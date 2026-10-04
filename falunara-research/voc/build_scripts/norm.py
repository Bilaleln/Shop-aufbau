import csv
SRC='/home/user/Shop-aufbau/falunara-research/voc/VOC3_raw_merged.csv'
MAP={
 'new_body_neglect_vs_face':'body_neglect_vs_face','new_body_neglect':'body_neglect_vs_face',
 'new_face_product_transfer':'face_product_transfer','new_face_products_on_body':'face_product_transfer',
 'new_reptile_metaphor':'texture_metaphor','new_desert_metaphor':'texture_metaphor','new_raisin_metaphor':'texture_metaphor',
 'new_mummy_metaphor':'texture_metaphor','new_leathery_skin':'texture_metaphor',
 'new_ingredient_fear':'ingredient_fear_clean','new_clean_ingredients':'ingredient_fear_clean','new_mineral_oil_distrust':'ingredient_fear_clean','new_ingredient_app':'ingredient_fear_clean',
 'new_reformulation_distrust':'reformulation_counterfeit_distrust','new_counterfeit_worry':'reformulation_counterfeit_distrust','new_amazon_counterfeit':'reformulation_counterfeit_distrust',
 'new_seeding_suspected':'marketing_distrust',
 'new_dry_climate':'climate_dryness','new_humidity_climate':'climate_dryness',
 'new_hot_shower':'shower_bath_shaving_trigger','new_hot_bath_trigger':'shower_bath_shaving_trigger','new_daily_shower':'shower_bath_shaving_trigger','new_shaving_trigger':'shower_bath_shaving_trigger',
 'new_sticky_sheets':'sticky_film_texture','new_waxy_texture':'sticky_film_texture',
 'new_lightweight_texture':'texture_weight_preference','new_rich_texture':'texture_weight_preference','new_oil_viscosity':'texture_weight_preference','new_skin_feel':'texture_weight_preference',
 'new_hydration_water':'hydration_water_belief','new_hydration_water_belief':'hydration_water_belief','new_hydration_myth':'hydration_water_belief','new_dehydrated_framing':'hydration_water_belief','new_thirsty_skin':'hydration_water_belief',
 'new_natural_oil_pref':'natural_botanical_pref','new_botanical_origin':'natural_botanical_pref','new_tallow':'natural_botanical_pref','new_formulated_vs_diy':'natural_botanical_pref','new_diy_mix':'natural_botanical_pref',
 'new_slippery_shower':'oil_shower_packaging_friction','new_packaging':'oil_shower_packaging_friction','new_packaging_dispenser':'oil_shower_packaging_friction',
 'new_sample_trial':'trial_before_commit','new_impulse_purchase':'trial_before_commit','new_patch_test_caution':'trial_before_commit',
 'new_competitor_oil':'competitor_body_oil',
 'question_oil_or_lotion':'oil_vs_lotion_confusion',
 'new_body_firmness':'firmness_desire','new_firming_claim':'firmness_desire',
 'new_mirror_trigger':'mirror_partner_moment','new_partner_reaction':'mirror_partner_moment',
 'new_invisibility':'invisibility_alienation','new_age_community_alienation':'invisibility_alienation','new_tribe_belonging':'invisibility_alienation',
 'new_night_sweats':'menopause_symptom_context',
 'new_unprepared':'betrayal_unprepared','new_betrayal':'betrayal_unprepared','new_dismissed_by_doctors':'betrayal_unprepared','new_gender_unfairness':'betrayal_unprepared',
 'new_crepey_abdomen':'crepey_abdomen',
 'new_crepefication':'crepey_wording','new_creepy_spelling':'crepey_wording',
 'new_strawberry_legs':'kp_strawberry_bumps','new_kp_bumps':'kp_strawberry_bumps',
 'new_peptides':'other_actives_beliefs','new_barrier_repair':'other_actives_beliefs','new_salicylic_body':'other_actives_beliefs','new_ingredient_belief':'other_actives_beliefs','new_silicone_in_oil':'other_actives_beliefs',
 'new_exercise_debate':'exercise_vs_topicals','new_topical_only':'topical_only_preference',
 'new_cleanser_focus':'cleanser_soap_focus','new_soap_free':'cleanser_soap_focus','new_rinse_off_doubt':'cleanser_soap_focus',
 'new_mature_skin_label':'mature_skin_label','new_ethics':'ethics_cruelty_free',
}
def split(s): return [x.strip() for x in s.replace(',',';').split(';') if x.strip()]
def load():
    rows=list(csv.DictReader(open(SRC,encoding='utf-8')))
    for r in rows:
        tags=[]
        for t in split(r['Recurrence/pattern tag']):
            n=MAP.get(t, t[4:] if t.startswith('new_') else t)
            if n not in tags: tags.append(n)
        r['tags']=tags; r['flags']=split(r['Flags'])
    return rows
