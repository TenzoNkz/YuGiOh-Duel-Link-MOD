# APKPure Original vs Platinmods — Static Variant Comparison

Generated: 2026-10-27 05:09:20 UTC
Purpose: APKPure Original is the sole intended mod base. Platinmods is a comparison reference only.
Method: Release digest checks, primary APK resolution, archive entry inventory, and per-entry SHA-256 comparison. No app was installed or executed.

## Source identity
### APKPure Original — intended modification base
- Release page: https://github.com/TenzoNkz/YuGiOh-Duel-Link-MOD/releases/tag/APKPure_Latest
- Release tag: APKPure_Latest
- Asset: Yu-Gi-Oh.Duel.Links.APKPure.V11.1.0.xapk
- Downloaded container size: 92,726,986 bytes (88.43 MiB)
- Expected container SHA-256: 66ba31c32fbba03b5fe0f75ef27dd9fa875978de7921a0c4ee8b93b878ce64eb
- Calculated container SHA-256: 66ba31c32fbba03b5fe0f75ef27dd9fa875978de7921a0c4ee8b93b878ce64eb
- GitHub digest comparison: True
- Container type: XAPK
- Selected primary APK member: jp.konami.duellinks.apk
- Selected primary APK size: 55,854,706 bytes (53.27 MiB)
- Selected primary APK SHA-256: e2f38c25eb8d32c66f6b2a036cbe1eeb44164841f6cb684073d9f5ea1ac0c11d
- Physical APK members inventoried: 2
- Logical package entries across primary and split payloads: 3377
- Aggregate uncompressed payload size (unique paths): 211,539,350 bytes (201.74 MiB)
- DEX count across logical package: 3
- Native library count across primary and split payloads: 9
- IL2CPP metadata files found by filename: 1
- Signature-related entries in merged payload inventory: 2
- Embedded APK members:
  - config.arm64_v8a.apk (36,869,159 bytes (35.16 MiB)); outer-container CRC: PASS; inner ZIP: PASS
  - jp.konami.duellinks.apk (55,854,706 bytes (53.27 MiB)); outer-container CRC: PASS; inner ZIP: PASS
- Selected primary APK member outer-container CRC: PASS

### Platinmods — reference only
- Release page: https://github.com/TenzoNkz/YuGiOh-Duel-Link-MOD/releases/tag/Latest
- Release tag: Latest
- Asset: Yu-Gi-Oh.Duel.Links.Platinmods.V11.1.0.apk
- Downloaded container size: 127,838,704 bytes (121.92 MiB)
- Expected container SHA-256: dc18ce334c18577195904b1461f9dfe68cf912182a06d85ee3e63fe6f1575c31
- Calculated container SHA-256: dc18ce334c18577195904b1461f9dfe68cf912182a06d85ee3e63fe6f1575c31
- GitHub digest comparison: True
- Container type: APK
- Selected primary APK member: Yu-Gi-Oh.Duel.Links.Platinmods.V11.1.0.apk
- Selected primary APK size: 127,838,704 bytes (121.92 MiB)
- Selected primary APK SHA-256: dc18ce334c18577195904b1461f9dfe68cf912182a06d85ee3e63fe6f1575c31
- Physical APK members inventoried: 1
- Logical package entries across primary and split payloads: 3398
- Aggregate uncompressed payload size (unique paths): 322,975,546 bytes (308.01 MiB)
- DEX count across logical package: 3
- Native library count across primary and split payloads: 20
- IL2CPP metadata files found by filename: 1
- Signature-related entries in merged payload inventory: 2

## Comparison summary
- Shared entry paths: 3081
- Shared entries with identical SHA-256: 2876
- Shared entries with different SHA-256: 205
- Shared entries with at least one unreadable/corrupt member: 0
- Unreadable/corrupt entries across APKPure main/split APKs: 0
- Unreadable/corrupt entries in Platinmods APK: 0
- APKPure-only entries: 296
- Platinmods-only entries: 317

## Key package and executable entries
| Entry path | APKPure bytes | Platinmods bytes | Result |
|---|---:|---:|---|
| AndroidManifest.xml | 24744 | 24584 | DIFFERENT |
| classes.dex | 7574408 | 7301956 | DIFFERENT |
| classes2.dex | 7094488 | 6866208 | DIFFERENT |
| classes3.dex | 2076 | 82316 | DIFFERENT |
| lib/arm64-v8a/libplatinmods.so | — | 9502424 | PLATINMODS_ONLY |
| lib/armeabi-v7a/libplatinmods.so | — | 8956032 | PLATINMODS_ONLY |
| lib/arm64-v8a/libduel.so | 22315680 | 22315680 | IDENTICAL |
| lib/armeabi-v7a/libduel.so | — | 19084176 | PLATINMODS_ONLY |
| lib/arm64-v8a/libil2cpp.so | 64335248 | 64335248 | IDENTICAL |
| lib/armeabi-v7a/libil2cpp.so | — | 54632964 | PLATINMODS_ONLY |
| assets/bin/Data/Managed/Metadata/global-metadata.dat | 11183816 | 11183816 | IDENTICAL |

## Highest-priority differing entries
| Entry path | APKPure bytes | Platinmods bytes | Classification |
|---|---:|---:|---|
| classes.dex | 7,574,408 | 7,301,956 | DEX/code |
| classes2.dex | 7,094,488 | 6,866,208 | DEX/code |
| classes3.dex | 2,076 | 82,316 | DEX/code |
| AndroidManifest.xml | 24,744 | 24,584 | manifest/resources/assets |
| resources.arsc | 438,004 | 437,028 | manifest/resources/assets |
| META-INF/BNDLTOOL.SF | 404,631 | 406,917 | manifest/resources/assets |
| META-INF/MANIFEST.MF | 404,504 | 406,790 | manifest/resources/assets |
| res/layout/abc_search_view.xml | 3,472 | 3,472 | manifest/resources/assets |
| res/layout/notification_template_big_media_narrow_custom.xml | 3,216 | 3,216 | manifest/resources/assets |
| res/layout/preference_widget_seekbar_material.xml | 3,056 | 3,056 | manifest/resources/assets |
| res/layout/notification_template_big_media_custom.xml | 3,044 | 3,044 | manifest/resources/assets |
| res/layout/preference_widget_seekbar.xml | 2,896 | 2,896 | manifest/resources/assets |
| res/layout/notification_template_lines_media.xml | 2,872 | 2,872 | manifest/resources/assets |
| res/anim/btn_checkbox_to_checked_box_outer_merged_animation.xml | 2,780 | 2,780 | manifest/resources/assets |
| res/layout/notification_template_media_custom.xml | 2,756 | 2,756 | manifest/resources/assets |
| res/drawable/btn_checkbox_checked_mtrl.xml | 2,688 | 2,688 | manifest/resources/assets |
| res/drawable/btn_checkbox_unchecked_mtrl.xml | 2,660 | 2,660 | manifest/resources/assets |
| res/layout/abc_alert_dialog_material.xml | 2,648 | 2,648 | manifest/resources/assets |
| res/layout/preference_dropdown.xml | 2,544 | 2,544 | manifest/resources/assets |
| res/anim/btn_checkbox_to_unchecked_check_path_merged_animation.xml | 2,520 | 2,520 | manifest/resources/assets |
| res/anim/btn_checkbox_to_unchecked_box_inner_merged_animation.xml | 2,360 | 2,360 | manifest/resources/assets |
| res/layout/preference.xml | 2,352 | 2,352 | manifest/resources/assets |
| res/anim/btn_checkbox_to_checked_box_inner_merged_animation.xml | 2,124 | 2,124 | manifest/resources/assets |
| res/layout/abc_popup_menu_item_layout.xml | 2,072 | 2,072 | manifest/resources/assets |
| res/layout/preference_information_material.xml | 2,056 | 2,056 | manifest/resources/assets |
| res/layout/preference_material.xml | 2,052 | 2,052 | manifest/resources/assets |
| res/layout/abc_search_dropdown_item_icons_2line.xml | 1,916 | 1,916 | manifest/resources/assets |
| res/layout/abc_cascading_menu_item_layout.xml | 1,868 | 1,868 | manifest/resources/assets |
| res/layout/notification_template_big_media_narrow.xml | 1,824 | 1,824 | manifest/resources/assets |
| res/layout/preference_category_material.xml | 1,768 | 1,768 | manifest/resources/assets |
| res/layout/preference_information.xml | 1,732 | 1,732 | manifest/resources/assets |
| res/drawable/btn_radio_off_mtrl.xml | 1,728 | 1,728 | manifest/resources/assets |
| META-INF/BNDLTOOL.RSA | 1,581 | 1,722 | manifest/resources/assets |
| res/layout/expand_button.xml | 1,720 | 1,720 | manifest/resources/assets |
| res/layout/notification_template_big_media.xml | 1,696 | 1,696 | manifest/resources/assets |
| res/layout/abc_activity_chooser_view.xml | 1,684 | 1,684 | manifest/resources/assets |
| res/anim/btn_radio_to_off_mtrl_dot_group_animation.xml | 1,656 | 1,656 | manifest/resources/assets |
| res/anim/btn_radio_to_off_mtrl_ring_outer_animation.xml | 1,656 | 1,656 | manifest/resources/assets |
| res/anim/btn_radio_to_on_mtrl_dot_group_animation.xml | 1,656 | 1,656 | manifest/resources/assets |
| res/anim/btn_radio_to_on_mtrl_ring_outer_animation.xml | 1,656 | 1,656 | manifest/resources/assets |
| res/drawable/btn_radio_on_mtrl.xml | 1,656 | 1,656 | manifest/resources/assets |
| res/layout/abc_alert_dialog_button_bar_material.xml | 1,584 | 1,584 | manifest/resources/assets |
| res/layout-v26/abc_screen_toolbar.xml | 1,560 | 1,560 | manifest/resources/assets |
| res/layout/abc_alert_dialog_title_material.xml | 1,560 | 1,560 | manifest/resources/assets |
| res/layout/abc_screen_toolbar.xml | 1,504 | 1,504 | manifest/resources/assets |
| res/drawable/abc_seekbar_track_material.xml | 1,408 | 1,408 | manifest/resources/assets |
| res/layout/abc_list_menu_item_layout.xml | 1,396 | 1,396 | manifest/resources/assets |
| res/layout/abc_activity_chooser_view_list_item.xml | 1,304 | 1,304 | manifest/resources/assets |
| res/layout/notification_template_media.xml | 1,292 | 1,292 | manifest/resources/assets |
| res/layout/preference_dialog_edittext.xml | 1,272 | 1,272 | manifest/resources/assets |
| res/anim/btn_checkbox_to_checked_icon_null_animation.xml | 1,196 | 1,196 | manifest/resources/assets |
| res/anim/btn_checkbox_to_unchecked_icon_null_animation.xml | 1,196 | 1,196 | manifest/resources/assets |
| res/drawable/abc_spinner_textfield_background_material.xml | 1,160 | 1,160 | manifest/resources/assets |
| res/drawable/common_google_signin_btn_text_disabled.xml | 1,152 | 1,152 | manifest/resources/assets |
| res/drawable/common_google_signin_btn_icon_disabled.xml | 1,132 | 1,132 | manifest/resources/assets |
| res/layout/abc_dialog_title_material.xml | 1,116 | 1,116 | manifest/resources/assets |
| res/drawable/abc_seekbar_thumb_material.xml | 1,100 | 1,100 | manifest/resources/assets |
| res/drawable/abc_ic_menu_cut_mtrl_alpha.xml | 1,096 | 1,096 | manifest/resources/assets |
| res/layout/image_frame.xml | 1,088 | 1,088 | manifest/resources/assets |
| res/drawable/abc_list_selector_holo_dark.xml | 1,064 | 1,064 | manifest/resources/assets |
| res/drawable/abc_list_selector_holo_light.xml | 1,064 | 1,064 | manifest/resources/assets |
| res/layout/abc_tooltip.xml | 1,056 | 1,056 | manifest/resources/assets |
| res/anim/btn_radio_to_off_mtrl_ring_outer_path_animation.xml | 1,028 | 1,028 | manifest/resources/assets |
| res/anim/btn_radio_to_on_mtrl_ring_outer_path_animation.xml | 1,028 | 1,028 | manifest/resources/assets |
| res/layout/abc_select_dialog_material.xml | 1,020 | 1,020 | manifest/resources/assets |
| res/drawable/abc_item_background_holo_dark.xml | 1,012 | 1,012 | manifest/resources/assets |
| res/drawable/abc_item_background_holo_light.xml | 1,012 | 1,012 | manifest/resources/assets |
| res/drawable/abc_ic_arrow_drop_right_black_24dp.xml | 1,000 | 1,000 | manifest/resources/assets |
| res/drawable/abc_ic_menu_share_mtrl_alpha.xml | 980 | 980 | manifest/resources/assets |
| res/drawable/abc_btn_default_mtrl_shape.xml | 932 | 932 | manifest/resources/assets |
| res/drawable/abc_ic_menu_selectall_mtrl_alpha.xml | 920 | 920 | manifest/resources/assets |
| res/drawable/common_google_signin_btn_icon_dark_focused.xml | 892 | 892 | manifest/resources/assets |
| res/drawable/common_google_signin_btn_icon_light_focused.xml | 892 | 892 | manifest/resources/assets |
| res/drawable/common_google_signin_btn_text_dark_focused.xml | 892 | 892 | manifest/resources/assets |
| res/drawable/common_google_signin_btn_text_light_focused.xml | 892 | 892 | manifest/resources/assets |
| res/layout/abc_action_bar_title_item.xml | 872 | 872 | manifest/resources/assets |
| res/layout/select_dialog_multichoice_material.xml | 864 | 864 | manifest/resources/assets |
| res/layout/select_dialog_singlechoice_material.xml | 864 | 864 | manifest/resources/assets |
| res/anim/abc_grow_fade_in_from_bottom.xml | 852 | 852 | manifest/resources/assets |
| res/anim/abc_shrink_fade_out_from_bottom.xml | 852 | 852 | manifest/resources/assets |
| res/layout/abc_popup_menu_header_item_layout.xml | 848 | 848 | manifest/resources/assets |
| res/layout/abc_action_mode_close_item_material.xml | 840 | 840 | manifest/resources/assets |
| res/layout/abc_screen_simple.xml | 832 | 832 | manifest/resources/assets |
| res/drawable/abc_ic_voice_search_api_material.xml | 828 | 828 | manifest/resources/assets |
| res/drawable/abc_btn_check_material_anim.xml | 816 | 816 | manifest/resources/assets |
| res/drawable/abc_btn_radio_material_anim.xml | 816 | 816 | manifest/resources/assets |
| res/drawable/abc_ic_search_api_material.xml | 812 | 812 | manifest/resources/assets |
| res/layout/preference_list_fragment.xml | 812 | 812 | manifest/resources/assets |
| res/drawable/abc_ic_menu_paste_mtrl_am_alpha.xml | 796 | 796 | manifest/resources/assets |
| res/drawable/abc_ic_menu_overflow_material.xml | 792 | 792 | manifest/resources/assets |
| res/layout/abc_screen_simple_overlay_action_mode.xml | 792 | 792 | manifest/resources/assets |
| res/layout/abc_list_menu_item_icon.xml | 780 | 780 | manifest/resources/assets |
| res/layout/abc_action_menu_item_layout.xml | 768 | 768 | manifest/resources/assets |
| res/drawable/abc_ic_menu_copy_mtrl_am_alpha.xml | 756 | 756 | manifest/resources/assets |
| res/drawable/abc_textfield_search_material.xml | 756 | 756 | manifest/resources/assets |
| res/layout/notification_media_cancel_action.xml | 744 | 744 | manifest/resources/assets |
| res/color/common_google_signin_btn_text_dark.xml | 712 | 712 | manifest/resources/assets |
| res/color/common_google_signin_btn_text_light.xml | 712 | 712 | manifest/resources/assets |
| res/layout/preference_dropdown_material.xml | 712 | 712 | manifest/resources/assets |
| res/xml/com_android_billingclient_phenotype.xml | 704 | 704 | manifest/resources/assets |

## Shared entries with unreadable/corrupt content (first 60)
- None found.

## APKPure-only entries (first 60)
- res/color-v23/abc_btn_colored_borderless_text_material.xml — 500 bytes (0.00 MiB)
- res/color-v23/abc_btn_colored_text_material.xml — 500 bytes (0.00 MiB)
- res/color-v23/abc_color_highlight_material.xml — 544 bytes (0.00 MiB)
- res/color-v23/abc_tint_btn_checkable.xml — 624 bytes (0.00 MiB)
- res/color-v23/abc_tint_default.xml — 1,120 bytes (0.00 MiB)
- res/color-v23/abc_tint_edittext.xml — 668 bytes (0.00 MiB)
- res/color-v23/abc_tint_seek_thumb.xml — 500 bytes (0.00 MiB)
- res/color-v23/abc_tint_spinner.xml — 668 bytes (0.00 MiB)
- res/color-v23/abc_tint_switch_track.xml — 664 bytes (0.00 MiB)
- res/drawable-hdpi-v4/abc_ab_share_pack_mtrl_alpha.9.png — 272 bytes (0.00 MiB)
- res/drawable-hdpi-v4/abc_btn_check_to_on_mtrl_000.png — 227 bytes (0.00 MiB)
- res/drawable-hdpi-v4/abc_btn_check_to_on_mtrl_015.png — 404 bytes (0.00 MiB)
- res/drawable-hdpi-v4/abc_btn_radio_to_on_mtrl_000.png — 464 bytes (0.00 MiB)
- res/drawable-hdpi-v4/abc_btn_radio_to_on_mtrl_015.png — 563 bytes (0.00 MiB)
- res/drawable-hdpi-v4/abc_btn_switch_to_on_mtrl_00001.9.png — 1,096 bytes (0.00 MiB)
- res/drawable-hdpi-v4/abc_btn_switch_to_on_mtrl_00012.9.png — 1,243 bytes (0.00 MiB)
- res/drawable-hdpi-v4/abc_cab_background_top_mtrl_alpha.9.png — 226 bytes (0.00 MiB)
- res/drawable-hdpi-v4/abc_ic_commit_search_api_mtrl_alpha.png — 171 bytes (0.00 MiB)
- res/drawable-hdpi-v4/abc_list_divider_mtrl_alpha.9.png — 167 bytes (0.00 MiB)
- res/drawable-hdpi-v4/abc_list_focused_holo.9.png — 244 bytes (0.00 MiB)
- res/drawable-hdpi-v4/abc_list_longpressed_holo.9.png — 212 bytes (0.00 MiB)
- res/drawable-hdpi-v4/abc_list_pressed_holo_dark.9.png — 208 bytes (0.00 MiB)
- res/drawable-hdpi-v4/abc_list_pressed_holo_light.9.png — 208 bytes (0.00 MiB)
- res/drawable-hdpi-v4/abc_list_selector_disabled_holo_dark.9.png — 228 bytes (0.00 MiB)
- res/drawable-hdpi-v4/abc_list_selector_disabled_holo_light.9.png — 229 bytes (0.00 MiB)
- res/drawable-hdpi-v4/abc_menu_hardkey_panel_mtrl_mult.9.png — 738 bytes (0.00 MiB)
- res/drawable-hdpi-v4/abc_popup_background_mtrl_mult.9.png — 1,098 bytes (0.00 MiB)
- res/drawable-hdpi-v4/abc_scrubber_control_off_mtrl_alpha.png — 201 bytes (0.00 MiB)
- res/drawable-hdpi-v4/abc_scrubber_control_to_pressed_mtrl_000.png — 196 bytes (0.00 MiB)
- res/drawable-hdpi-v4/abc_scrubber_control_to_pressed_mtrl_005.png — 272 bytes (0.00 MiB)
- res/drawable-hdpi-v4/abc_scrubber_primary_mtrl_alpha.9.png — 205 bytes (0.00 MiB)
- res/drawable-hdpi-v4/abc_scrubber_track_mtrl_alpha.9.png — 196 bytes (0.00 MiB)
- res/drawable-hdpi-v4/abc_spinner_mtrl_am_alpha.9.png — 345 bytes (0.00 MiB)
- res/drawable-hdpi-v4/abc_switch_track_mtrl_alpha.9.png — 484 bytes (0.00 MiB)
- res/drawable-hdpi-v4/abc_tab_indicator_mtrl_alpha.9.png — 190 bytes (0.00 MiB)
- res/drawable-hdpi-v4/abc_text_select_handle_left_mtrl.png — 278 bytes (0.00 MiB)
- res/drawable-hdpi-v4/abc_text_select_handle_middle_mtrl.png — 396 bytes (0.00 MiB)
- res/drawable-hdpi-v4/abc_text_select_handle_right_mtrl.png — 262 bytes (0.00 MiB)
- res/drawable-hdpi-v4/abc_textfield_activated_mtrl_alpha.9.png — 186 bytes (0.00 MiB)
- res/drawable-hdpi-v4/abc_textfield_default_mtrl_alpha.9.png — 192 bytes (0.00 MiB)
- res/drawable-hdpi-v4/abc_textfield_search_activated_mtrl_alpha.9.png — 178 bytes (0.00 MiB)
- res/drawable-hdpi-v4/abc_textfield_search_default_mtrl_alpha.9.png — 178 bytes (0.00 MiB)
- res/drawable-hdpi-v4/common_full_open_on_phone.png — 681 bytes (0.00 MiB)
- res/drawable-hdpi-v4/common_google_signin_btn_icon_dark_normal_background.9.png — 897 bytes (0.00 MiB)
- res/drawable-hdpi-v4/common_google_signin_btn_icon_light_normal_background.9.png — 683 bytes (0.00 MiB)
- res/drawable-hdpi-v4/common_google_signin_btn_text_dark_normal_background.9.png — 960 bytes (0.00 MiB)
- res/drawable-hdpi-v4/common_google_signin_btn_text_light_normal_background.9.png — 694 bytes (0.00 MiB)
- res/drawable-hdpi-v4/googleg_disabled_color_18.png — 410 bytes (0.00 MiB)
- res/drawable-hdpi-v4/googleg_standard_color_18.png — 808 bytes (0.00 MiB)
- res/drawable-hdpi-v4/ic_notify.png — 532 bytes (0.00 MiB)
- res/drawable-hdpi-v4/notification_bg_low_normal.9.png — 212 bytes (0.00 MiB)
- res/drawable-hdpi-v4/notification_bg_low_pressed.9.png — 225 bytes (0.00 MiB)
- res/drawable-hdpi-v4/notification_bg_normal.9.png — 212 bytes (0.00 MiB)
- res/drawable-hdpi-v4/notification_bg_normal_pressed.9.png — 225 bytes (0.00 MiB)
- res/drawable-hdpi-v4/notify_panel_notification_icon_bg.png — 107 bytes (0.00 MiB)
- res/drawable-ldrtl-hdpi-v17/abc_spinner_mtrl_am_alpha.9.png — 345 bytes (0.00 MiB)
- res/drawable-ldrtl-mdpi-v17/abc_spinner_mtrl_am_alpha.9.png — 318 bytes (0.00 MiB)
- res/drawable-ldrtl-xhdpi-v17/abc_spinner_mtrl_am_alpha.9.png — 417 bytes (0.00 MiB)
- res/drawable-ldrtl-xxhdpi-v17/abc_spinner_mtrl_am_alpha.9.png — 525 bytes (0.00 MiB)
- res/drawable-ldrtl-xxxhdpi-v17/abc_spinner_mtrl_am_alpha.9.png — 437 bytes (0.00 MiB)

## Platinmods-only entries (first 60)
- META-INF/activity_release.kotlin_module — 137 bytes (0.00 MiB)
- META-INF/annotation.kotlin_module — 24 bytes (0.00 MiB)
- META-INF/appcompat_release.kotlin_module — 24 bytes (0.00 MiB)
- META-INF/core-ktx_release.kotlin_module — 1,150 bytes (0.00 MiB)
- META-INF/core_release.kotlin_module — 24 bytes (0.00 MiB)
- META-INF/kotlin-stdlib-common.kotlin_module — 1,623 bytes (0.00 MiB)
- META-INF/kotlin-stdlib.kotlin_module — 6,937 bytes (0.01 MiB)
- META-INF/lifecycle-viewmodel-savedstate_release.kotlin_module — 101 bytes (0.00 MiB)
- META-INF/lifecycle-viewmodel_release.kotlin_module — 154 bytes (0.00 MiB)
- META-INF/savedstate_release.kotlin_module — 80 bytes (0.00 MiB)
- assets/platinmodsRB.png — 4,775 bytes (0.00 MiB)
- lib/arm64-v8a/libplatinmods.so — 9,502,424 bytes (9.06 MiB)
- lib/armeabi-v7a/libFirebaseCppAnalytics.so — 50,804 bytes (0.05 MiB)
- lib/armeabi-v7a/libFirebaseCppApp-13_4_0.so — 3,299,184 bytes (3.15 MiB)
- lib/armeabi-v7a/libFirebaseCppMessaging.so — 50,864 bytes (0.05 MiB)
- lib/armeabi-v7a/lib_burst_generated.so — 24,468 bytes (0.02 MiB)
- lib/armeabi-v7a/libdatastore_shared_counter.so — 4,416 bytes (0.00 MiB)
- lib/armeabi-v7a/libduel.so — 19,084,176 bytes (18.20 MiB)
- lib/armeabi-v7a/libil2cpp.so — 54,632,964 bytes (52.10 MiB)
- lib/armeabi-v7a/libmain.so — 8,260 bytes (0.01 MiB)
- lib/armeabi-v7a/libplatinmods.so — 8,956,032 bytes (8.54 MiB)
- lib/armeabi-v7a/libunity.so — 16,232,828 bytes (15.48 MiB)
- res/  — 107 bytes (0.00 MiB)
- res/color/abc_btn_colored_borderless_text_material.xml — 500 bytes (0.00 MiB)
- res/color/abc_btn_colored_text_material.xml — 500 bytes (0.00 MiB)
- res/color/abc_color_highlight_material.xml — 544 bytes (0.00 MiB)
- res/color/abc_tint_btn_checkable.xml — 624 bytes (0.00 MiB)
- res/color/abc_tint_default.xml — 1,120 bytes (0.00 MiB)
- res/color/abc_tint_edittext.xml — 668 bytes (0.00 MiB)
- res/color/abc_tint_seek_thumb.xml — 500 bytes (0.00 MiB)
- res/color/abc_tint_spinner.xml — 668 bytes (0.00 MiB)
- res/color/abc_tint_switch_track.xml — 664 bytes (0.00 MiB)
- res/drawable-hdpi/abc_ab_share_pack_mtrl_alpha.9.png — 272 bytes (0.00 MiB)
- res/drawable-hdpi/abc_btn_check_to_on_mtrl_000.png — 227 bytes (0.00 MiB)
- res/drawable-hdpi/abc_btn_check_to_on_mtrl_015.png — 404 bytes (0.00 MiB)
- res/drawable-hdpi/abc_btn_radio_to_on_mtrl_000.png — 464 bytes (0.00 MiB)
- res/drawable-hdpi/abc_btn_radio_to_on_mtrl_015.png — 563 bytes (0.00 MiB)
- res/drawable-hdpi/abc_btn_switch_to_on_mtrl_00001.9.png — 1,096 bytes (0.00 MiB)
- res/drawable-hdpi/abc_btn_switch_to_on_mtrl_00012.9.png — 1,243 bytes (0.00 MiB)
- res/drawable-hdpi/abc_cab_background_top_mtrl_alpha.9.png — 226 bytes (0.00 MiB)
- res/drawable-hdpi/abc_ic_commit_search_api_mtrl_alpha.png — 171 bytes (0.00 MiB)
- res/drawable-hdpi/abc_list_divider_mtrl_alpha.9.png — 167 bytes (0.00 MiB)
- res/drawable-hdpi/abc_list_focused_holo.9.png — 258 bytes (0.00 MiB)
- res/drawable-hdpi/abc_list_longpressed_holo.9.png — 212 bytes (0.00 MiB)
- res/drawable-hdpi/abc_list_pressed_holo_dark.9.png — 208 bytes (0.00 MiB)
- res/drawable-hdpi/abc_list_pressed_holo_light.9.png — 208 bytes (0.00 MiB)
- res/drawable-hdpi/abc_list_selector_disabled_holo_dark.9.png — 228 bytes (0.00 MiB)
- res/drawable-hdpi/abc_list_selector_disabled_holo_light.9.png — 229 bytes (0.00 MiB)
- res/drawable-hdpi/abc_menu_hardkey_panel_mtrl_mult.9.png — 738 bytes (0.00 MiB)
- res/drawable-hdpi/abc_popup_background_mtrl_mult.9.png — 1,098 bytes (0.00 MiB)
- res/drawable-hdpi/abc_scrubber_control_off_mtrl_alpha.png — 201 bytes (0.00 MiB)
- res/drawable-hdpi/abc_scrubber_control_to_pressed_mtrl_000.png — 196 bytes (0.00 MiB)
- res/drawable-hdpi/abc_scrubber_control_to_pressed_mtrl_005.png — 272 bytes (0.00 MiB)
- res/drawable-hdpi/abc_scrubber_primary_mtrl_alpha.9.png — 205 bytes (0.00 MiB)
- res/drawable-hdpi/abc_scrubber_track_mtrl_alpha.9.png — 196 bytes (0.00 MiB)
- res/drawable-hdpi/abc_spinner_mtrl_am_alpha.9.png — 345 bytes (0.00 MiB)
- res/drawable-hdpi/abc_switch_track_mtrl_alpha.9.png — 484 bytes (0.00 MiB)
- res/drawable-hdpi/abc_tab_indicator_mtrl_alpha.9.png — 190 bytes (0.00 MiB)
- res/drawable-hdpi/abc_text_select_handle_left_mtrl.png — 278 bytes (0.00 MiB)
- res/drawable-hdpi/abc_text_select_handle_middle_mtrl.png — 396 bytes (0.00 MiB)

## Limitations and interpretation
- No automatic integrity warning was raised. This does not prove any mod feature works.
- Different entry hashes prove byte differences only, not what changed semantically.
- APK v2/v3 signing blocks are not ordinary ZIP entries; this report does not verify signer identity or Android update compatibility.
- For XAPK input, the comparison merges the primary APK's logical entries with unique entries from extracted splits (including native libraries), while excluding split-specific manifests/signature metadata. It does not synthesize or validate a single installable APK.
- Current APKPure source-integrity blockers: both embedded APK outer CRC checks fail; one primary asset cannot decompress and the ARM64 libduel.so entry fails its inner CRC. Do not patch/build until a clean original XAPK is uploaded and passes analysis.
- The current APKPure XAPK contains integrity failures in the primary APK asset data and the arm64 libduel.so entry. Treat all features depending on those entries as unknown until a clean original package is uploaded.
- Platinmods is not the build base. Do not copy its binary components into CHATGPT MOD without independent technical review and necessary rights.

## Next reverse-engineering actions
1. Read APK_CODE_ANALYSIS.md for package, DEX, resource, and native-string findings from the APKPure primary APK.
2. Trace candidate features from menu label/resource through DEX callbacks into native dispatch where evidence permits.
3. Record verified facts, hypotheses, and test results separately in MOD_CANDIDATES.md.
4. Keep final APK patch/build blocked until the desired features and XAPK/split compatibility have evidence.

