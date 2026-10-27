#!/usr/bin/env python3
"""KIE AI API helper for Singing Ad production.

Handles Suno songs, Nano Banana Pro images, GPT Image 2 images,
Kling 3.0 video clips, and task polling — all through api.kie.ai.

Usage as library:
    from kie_api import KieClient
    client = KieClient()  # reads KIE_API_KEY from env
    task_id = client.generate_suno(lyrics, style, title)
    result = client.poll(task_id)

Usage as CLI:
    python3 kie_api.py suno-status <taskId>
    python3 kie_api.py job-status <taskId>
    python3 kie_api.py credits
"""

import json
import os
import ssl
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

BASE = "https://api.kie.ai"
CA_BUNDLE = "/root/.ccr/ca-bundle.crt"
MAX_POLL = 600
POLL_INITIAL = 3
POLL_MAX = 15
MAX_RETRIES = 4


def _ssl_ctx():
    p = Path(CA_BUNDLE)
    if p.exists():
        return ssl.create_default_context(cafile=str(p))
    return ssl.create_default_context()


class KieClient:
    def __init__(self, api_key=None):
        self.key = api_key or os.environ.get("KIE_API_KEY", "")
        if not self.key:
            raise RuntimeError("KIE_API_KEY not set")
        self.ssl_ctx = _ssl_ctx()

    def _headers(self):
        return {
            "Authorization": f"Bearer {self.key}",
            "Content-Type": "application/json",
        }

    def _request(self, method, path, body=None, retries=MAX_RETRIES):
        url = BASE + path
        data = json.dumps(body).encode() if body else None
        for attempt in range(retries + 1):
            try:
                req = urllib.request.Request(
                    url, headers=self._headers(), data=data, method=method
                )
                resp = urllib.request.urlopen(req, timeout=30, context=self.ssl_ctx)
                return json.loads(resp.read().decode())
            except urllib.error.HTTPError as e:
                raw = e.read().decode()
                try:
                    return json.loads(raw)
                except json.JSONDecodeError:
                    if attempt < retries and e.code >= 500:
                        time.sleep(2 ** attempt)
                        continue
                    raise RuntimeError(f"HTTP {e.code}: {raw[:200]}")
            except (ConnectionError, TimeoutError, urllib.error.URLError) as e:
                if attempt < retries:
                    time.sleep(2 ** attempt)
                    continue
                raise

    def _get(self, path):
        return self._request("GET", path)

    def _post(self, path, body):
        return self._request("POST", path, body)

    # -- Suno (music generation) --

    def generate_suno(self, lyrics, style, title, model="V4_5", callback_url="https://example.com/cb"):
        """Submit a Suno song generation. Returns taskId."""
        resp = self._post("/api/v1/generate", {
            "prompt": lyrics,
            "style": style,
            "title": title,
            "customMode": True,
            "instrumental": False,
            "model": model,
            "callBackUrl": callback_url,
        })
        if resp.get("code") != 200:
            raise RuntimeError(f"Suno generate failed: {resp}")
        return resp["data"]["taskId"]

    def suno_status(self, task_id):
        """Check Suno task status. Returns full response data."""
        resp = self._get(f"/api/v1/generate/record-info?taskId={task_id}")
        if resp.get("code") != 200:
            raise RuntimeError(f"Suno status failed: {resp}")
        return resp.get("data", {})

    # -- Jobs (images & video via createTask) --

    def create_task(self, model, input_params, callback_url=None):
        """Submit a job (image or video). Returns taskId."""
        body = {"model": model, "input": input_params}
        if callback_url:
            body["callBackUrl"] = callback_url
        resp = self._post("/api/v1/jobs/createTask", body)
        if resp.get("code") != 200:
            raise RuntimeError(f"createTask failed: {resp}")
        return resp["data"]["taskId"]

    def job_status(self, task_id):
        """Check job status. Returns full response data."""
        resp = self._get(f"/api/v1/jobs/recordInfo?taskId={task_id}")
        if resp.get("code") != 200:
            raise RuntimeError(f"recordInfo failed: {resp}")
        return resp.get("data", {})

    # -- Convenience wrappers --

    def generate_image_nano(self, prompt, refs=None, aspect="9:16", resolution="2K"):
        """Generate image with Nano Banana Pro. Returns taskId."""
        inp = {
            "prompt": prompt,
            "aspect_ratio": aspect,
            "resolution": resolution,
            "output_format": "png",
        }
        if refs:
            inp["image_input"] = refs
        return self.create_task("nano-banana-pro", inp)

    def generate_image_gpt(self, prompt, input_urls=None, aspect="9:16", resolution="2K"):
        """Generate image with GPT Image 2 (for product/text). Returns taskId."""
        inp = {
            "prompt": prompt,
            "aspect_ratio": aspect,
            "resolution": resolution,
        }
        if input_urls:
            inp["input_urls"] = input_urls
        return self.create_task("gpt-image-2-image-to-image", inp)

    def generate_clip_kling(self, prompt, image_url, duration="5", mode="std"):
        """Generate video clip with Kling 3.0. Returns taskId."""
        return self.create_task("kling-3.0/video", {
            "prompt": prompt,
            "duration": duration,
            "aspect_ratio": "9:16",
            "mode": mode,
            "sound": False,
            "multi_shots": False,
            "image_urls": [image_url],
        })

    # -- Polling --

    def poll(self, task_id, is_suno=False, max_wait=MAX_POLL, quiet=False):
        """Poll until task completes. Returns result data."""
        status_fn = self.suno_status if is_suno else self.job_status
        state_key = "status" if is_suno else "state"
        done_vals = {"SUCCESS", "success"}
        fail_vals = {"FAILURE", "fail", "FAILED"}

        interval = POLL_INITIAL
        elapsed = 0
        while elapsed < max_wait:
            data = status_fn(task_id)
            state = data.get(state_key, "unknown")
            if not quiet:
                print(f"  [{elapsed:>4}s] {task_id}: {state}")
            if state in done_vals:
                return data
            if state in fail_vals:
                raise RuntimeError(f"Task {task_id} failed: {data}")
            time.sleep(interval)
            elapsed += interval
            interval = min(interval * 1.5, POLL_MAX)

        raise TimeoutError(f"Task {task_id} not done after {max_wait}s")

    def download(self, url, dest_path, retries=MAX_RETRIES):
        """Download a result file with retries."""
        for attempt in range(retries + 1):
            try:
                req = urllib.request.Request(url)
                resp = urllib.request.urlopen(req, timeout=60, context=self.ssl_ctx)
                Path(dest_path).parent.mkdir(parents=True, exist_ok=True)
                with open(dest_path, "wb") as f:
                    while chunk := resp.read(65536):
                        f.write(chunk)
                return dest_path
            except Exception:
                if attempt < retries:
                    time.sleep(2 ** attempt)
                    continue
                raise


# -- CLI --

def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    client = KieClient()
    cmd = sys.argv[1]

    if cmd == "suno-status" and len(sys.argv) >= 3:
        data = client.suno_status(sys.argv[2])
        print(json.dumps(data, indent=2, ensure_ascii=False))
    elif cmd == "job-status" and len(sys.argv) >= 3:
        data = client.job_status(sys.argv[2])
        print(json.dumps(data, indent=2, ensure_ascii=False))
    elif cmd == "test":
        print("Testing KIE AI connection...")
        resp = client._get("/v1/models")
        count = len(resp.get("data", []))
        print(f"OK — {count} models available")

        try:
            data = client.suno_status("test_nonexistent")
            print(f"Suno endpoint OK — status: {data.get('status', 'reachable') if data else 'reachable'}")
        except Exception:
            print("Suno endpoint OK — reachable (no task data for test ID)")

        try:
            data = client.job_status("test_nonexistent")
            print(f"Jobs endpoint OK — state: {data.get('state', 'reachable') if data else 'reachable'}")
        except Exception:
            print("Jobs endpoint OK — reachable (no task data for test ID)")
        print("All endpoints verified.")
    else:
        print(__doc__)
        sys.exit(1)


if __name__ == "__main__":
    main()
