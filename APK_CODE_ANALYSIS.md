# APK Code Analysis Report

**Generated:** 2026-10-26 05:14:02 UTC
**Method:** JADX/Apktool static analysis; the APK was not installed or executed.
- Repository: TenzoNkz/YuGiOh-Duel-Link-MOD
- Requested release tag: Platinmods_V11.0.0
- JADX pinned version: 1.5.6
- Apktool pinned version: 3.0.3

## Source Release and integrity
- Release page: https://github.com/TenzoNkz/YuGiOh-Duel-Link-MOD/releases/tag/Platinmods_V11.0.0
- Release tag: Platinmods_V11.0.0
- APK asset: Yu-Gi-Oh.Duel.Links.Platinmods.V11.0.0.apk
- GitHub-reported size: 127424878 bytes
- Downloaded size: 127424878 bytes
- Expected SHA-256: d7855754afbfe8e6b0a5db51ba47e4cefcd3079631190c11478d6556e06c56fb
- Calculated SHA-256: d7855754afbfe8e6b0a5db51ba47e4cefcd3079631190c11478d6556e06c56fb
- Digest comparison: PASS

**Status:** CODE_ANALYSIS_PARTIAL

## Android manifest (decoded by Apktool)
- Package name: jp.konami.duellinks
- Version name: not declared
- Version code: not declared
- minSdkVersion: not declared
- targetSdkVersion: not declared

## Tool execution
- Apktool exit code: 0
- JADX exit code: 3
- Decompiled Java source files found: 8194
- Decoded Apktool output entries: 18765

### Apktool output excerpt
    I: Using Apktool 3.0.3 on source.apk with 4 threads
    I: Baksmaling classes.dex...
    I: Baksmaling classes2.dex...
    I: Baksmaling classes3.dex...
    I: Loading resource table...
    I: Decoding value resources...
    I: Loading resource table from file: /home/runner/.local/share/apktool/framework/1.apk
    I: Decoding file resources...
    I: Generating values XMLs...
    I: Decoding AndroidManifest.xml with resources...
    I: Copying original files...
    I: Copying assets...
    I: Copying lib...
    I: Copying unknown files...

### JADX output excerpt
    INFO  - progress: 7940 of 8893 (89%)
    INFO  - progress: 8001 of 8893 (89%)
    INFO  - progress: 8098 of 8893 (91%)
    INFO  - progress: 8153 of 8893 (91%)
    INFO  - progress: 8269 of 8893 (92%)
    INFO  - progress: 8424 of 8893 (94%)
    INFO  - progress: 8535 of 8893 (95%)
    INFO  - progress: 8535 of 8893 (95%)
    INFO  - progress: 8535 of 8893 (95%)
    INFO  - progress: 8535 of 8893 (95%)
    INFO  - progress: 8535 of 8893 (95%)
    INFO  - progress: 8535 of 8893 (95%)
    INFO  - progress: 8535 of 8893 (95%)
    INFO  - progress: 8535 of 8893 (95%)
    INFO  - progress: 8535 of 8893 (95%)
    INFO  - progress: 8535 of 8893 (95%)
    INFO  - progress: 8535 of 8893 (95%)
    INFO  - progress: 8535 of 8893 (95%)
    INFO  - progress: 8535 of 8893 (95%)
    INFO  - progress: 8535 of 8893 (95%)
    INFO  - progress: 8604 of 8893 (96%)
    INFO  - progress: 8795 of 8893 (98%)
                                                                 
    ERROR - finished with errors, count: 96

## Selected native/IL2CPP inventory
- assets/bin/Data/Managed/Metadata/global-metadata.dat: 11182904 bytes
- lib/arm64-v8a/libduel.so: 22185664 bytes
- lib/arm64-v8a/libil2cpp.so: 64327320 bytes
- lib/arm64-v8a/libplatinmods.so: 9289224 bytes
- lib/armeabi-v7a/libduel.so: 18973460 bytes
- lib/armeabi-v7a/libil2cpp.so: 54624932 bytes
- lib/armeabi-v7a/libplatinmods.so: 8744976 bytes

## Search hits in decompiled Java
- Matching lines found: 1275; displaying up to 100.
- resources/AndroidManifest.xml:319: android:name="com.platinmods.FloatingModMenuService"
- resources/AndroidManifest.xml:324: android:name="com.platinmods.PMLauncher"/>
- resources/res/drawable/abc_btn_colored_material.xml:6: android:insetBottom="@dimen/abc_button_inset_vertical_material">
- resources/res/drawable/abc_btn_colored_material.xml:18: android:bottom="@dimen/abc_button_padding_vertical_material"/>
- resources/res/drawable/abc_btn_colored_material.xml:29: android:bottom="@dimen/abc_button_padding_vertical_material"/>
- resources/res/drawable/abc_btn_default_mtrl_shape.xml:6: android:insetBottom="@dimen/abc_button_inset_vertical_material">
- resources/res/drawable/abc_btn_default_mtrl_shape.xml:14: android:bottom="@dimen/abc_button_padding_vertical_material"/>
- resources/res/drawable/abc_dialog_material_background.xml:6: android:insetBottom="16dp">
- resources/res/drawable/abc_edit_text_material.xml:6: android:insetBottom="@dimen/abc_edit_text_inset_bottom_material">
- resources/res/drawable/abc_spinner_textfield_background_material.xml:6: android:insetBottom="@dimen/abc_control_inset_material">
- resources/res/drawable/common_google_signin_btn_icon_dark_focused.xml:7: android:bottom="1dp">
- resources/res/drawable/common_google_signin_btn_icon_disabled.xml:7: android:bottom="3dp">
- resources/res/drawable/common_google_signin_btn_icon_disabled.xml:15: android:bottom="7dp"/>
- resources/res/drawable/common_google_signin_btn_icon_light_focused.xml:7: android:bottom="1dp">
- resources/res/drawable/common_google_signin_btn_text_dark_focused.xml:7: android:bottom="1dp">
- resources/res/drawable/common_google_signin_btn_text_disabled.xml:7: android:bottom="3dp">
- resources/res/drawable/common_google_signin_btn_text_disabled.xml:15: android:bottom="7dp"/>
- resources/res/drawable/common_google_signin_btn_text_light_focused.xml:7: android:bottom="1dp">
- resources/res/drawable/notification_action_background.xml:8: android:insetBottom="@dimen/compat_button_inset_vertical_material">
- resources/res/drawable/notification_action_background.xml:16: android:bottom="@dimen/compat_button_padding_vertical_material"/>
- resources/res/drawable-watch/common_google_signin_btn_text_disabled.xml:7: android:bottom="3dp">
- resources/res/drawable-watch/common_google_signin_btn_text_disabled.xml:14: android:bottom="7dp"/>
- resources/res/layout/abc_action_menu_item_layout.xml:10: android:paddingBottom="4dp"
- resources/res/layout/abc_activity_chooser_view.xml:16: android:paddingBottom="2dp"
- resources/res/layout/abc_activity_chooser_view.xml:36: android:paddingBottom="2dp"
- resources/res/layout/abc_alert_dialog_button_bar_material.xml:7: android:scrollIndicators="bottom|top"
- resources/res/layout/abc_alert_dialog_button_bar_material.xml:10: android:gravity="bottom"
- resources/res/layout/abc_alert_dialog_button_bar_material.xml:15: android:paddingBottom="4dp"
- resources/res/layout/abc_alert_dialog_material.xml:51: android:layout_gravity="bottom"
- resources/res/layout/abc_cascading_menu_item_layout.xml:13: android:layout_marginBottom="4dp"/>
- resources/res/layout/abc_list_menu_item_icon.xml:11: android:layout_marginBottom="8dp"
- resources/res/layout/abc_popup_menu_item_layout.xml:13: android:layout_marginBottom="4dp"/>
- resources/res/layout/abc_search_dropdown_item_icons_2line.xml:13: android:layout_alignParentBottom="true"
- resources/res/layout/abc_search_dropdown_item_icons_2line.xml:23: android:layout_alignParentBottom="true"
- resources/res/layout/abc_search_dropdown_item_icons_2line.xml:32: android:layout_alignParentBottom="true"
- resources/res/layout/abc_search_dropdown_item_icons_2line.xml:39: android:paddingBottom="4dp"
- resources/res/layout/abc_search_dropdown_item_icons_2line.xml:44: android:layout_alignParentBottom="true"
- resources/res/layout/abc_search_view.xml:15: android:layout_marginBottom="2dp"
- resources/res/layout/abc_select_dialog_material.xml:14: app:paddingBottomNoButtons="@dimen/abc_dialog_list_padding_bottom_no_buttons"
- resources/res/layout/abc_tooltip.xml:15: android:paddingBottom="@dimen/tooltip_vertical_padding"
- resources/res/layout/expand_button.xml:17: android:paddingBottom="16dp"
- resources/res/layout/image_frame.xml:9: android:paddingBottom="4dp"
- resources/res/layout/notification_template_big_media.xml:34: android:layout_alignParentBottom="true"
- resources/res/layout/notification_template_big_media_custom.xml:35: android:layout_marginBottom="8dp"
- resources/res/layout/notification_template_big_media_custom.xml:64: android:layout_gravity="end|bottom"
- resources/res/layout/notification_template_big_media_custom.xml:79: android:layout_alignParentBottom="true"
- resources/res/layout/notification_template_big_media_narrow.xml:35: android:layout_alignParentBottom="true"
- resources/res/layout/notification_template_big_media_narrow_custom.xml:36: android:layout_marginBottom="8dp"
- resources/res/layout/notification_template_big_media_narrow_custom.xml:65: android:layout_gravity="end|bottom"
- resources/res/layout/notification_template_big_media_narrow_custom.xml:81: android:layout_alignParentBottom="true"
- resources/res/layout/notification_template_custom_big.xml:26: android:layout_marginBottom="8dp"
- resources/res/layout/notification_template_custom_big.xml:51: android:layout_gravity="end|bottom"
- resources/res/layout/notification_template_icon_group.xml:11: android:layout_marginBottom="@dimen/notification_big_circle_margin"
- resources/res/layout/notification_template_icon_group.xml:16: android:layout_gravity="end|bottom"
- resources/res/layout/notification_template_icon_group.xml:21: android:layout_marginBottom="8dp"
- resources/res/layout/notification_template_lines_media.xml:6: android:paddingBottom="2dp"
- resources/res/layout/notification_template_lines_media.xml:60: android:layout_marginBottom="-2dp"
- resources/res/layout/notification_template_media_custom.xml:27: android:layout_marginBottom="8dp"
- resources/res/layout/notification_template_media_custom.xml:56: android:layout_gravity="end|bottom"
- resources/res/layout/preference.xml:27: android:layout_marginBottom="6dp"
- resources/res/layout/preference_category_material.xml:16: android:paddingBottom="8dp"
- resources/res/layout/preference_dialog_edittext.xml:6: android:layout_marginBottom="48dp"
- resources/res/layout/preference_dialog_edittext.xml:19: android:layout_marginBottom="48dp"
- resources/res/layout/preference_dropdown.xml:33: android:layout_marginBottom="6dp"
- resources/res/layout/preference_information.xml:15: android:layout_marginBottom="6sp"
- resources/res/layout/preference_information_material.xml:27: android:paddingBottom="16dp"
- resources/res/layout/preference_material.xml:17: android:paddingBottom="16dp"
- resources/res/layout/preference_recyclerview.xml:5: android:paddingBottom="0dp"
- resources/res/layout/preference_widget_seekbar.xml:25: android:layout_marginBottom="6dp"
- resources/res/layout/preference_widget_seekbar_material.xml:23: android:layout_marginBottom="8dp">
- resources/res/layout/preference_widget_seekbar_material.xml:64: android:paddingBottom="@dimen/preference_seekbar_padding_vertical"
- resources/res/layout-watch/abc_alert_dialog_button_bar_material.xml:3: android:gravity="bottom"
- resources/res/layout-watch/abc_alert_dialog_button_bar_material.xml:9: android:paddingBottom="4dp"
- resources/res/values/attrs.xml:143: <enum name="bottom" value="3" />
- resources/res/values/attrs.xml:165: <flag name="bottom" value="0x50" />
- resources/res/values/attrs.xml:287: <attr name="contentPaddingBottom" format="dimension">
- resources/res/values/attrs.xml:342: <attr name="drawableBottomCompat" format="reference">
- resources/res/values/attrs.xml:498: <attr name="lastBaselineToBottomHeight" format="dimension">
- resources/res/values/attrs.xml:507: <flag name="bottom" value="0x50" />
- resources/res/values/attrs.xml:533: <attr name="layout_constraintBottom_creator" format="integer">
- resources/res/values/attrs.xml:535: <attr name="layout_constraintBottom_toBottomOf" format="reference">
- resources/res/values/attrs.xml:538: <attr name="layout_constraintBottom_toTopOf" format="reference">
- resources/res/values/attrs.xml:607: <attr name="layout_constraintTop_toBottomOf" format="reference">
- resources/res/values/attrs.xml:637: <flag name="bottom" value="0x50" />
- resources/res/values/attrs.xml:649: <attr name="layout_goneMarginBottom" format="dimension">
- resources/res/values/attrs.xml:662: <enum name="bottom" value="0x50" />
- resources/res/values/attrs.xml:758: <attr name="paddingBottomNoButtons" format="dimension">
- resources/res/values/attrs.xml:991: <attr name="titleMarginBottom" format="dimension">
- resources/res/values/dimens.xml:14: <dimen name="abc_action_bar_subtitle_bottom_margin_material">5dp</dimen>
- resources/res/values/dimens.xml:35: <dimen name="abc_dialog_list_padding_bottom_no_buttons">8dp</dimen>
- resources/res/values/dimens.xml:47: <dimen name="abc_edit_text_inset_bottom_material">7dp</dimen>
- resources/res/values/public.xml:5: <public type="anim" name="abc_grow_fade_in_from_bottom" id="0x7f010002" />
- resources/res/values/public.xml:8: <public type="anim" name="abc_shrink_fade_out_from_bottom" id="0x7f010005" />
- resources/res/values/public.xml:9: <public type="anim" name="abc_slide_in_bottom" id="0x7f010006" />
- resources/res/values/public.xml:11: <public type="anim" name="abc_slide_out_bottom" id="0x7f010008" />
- resources/res/values/public.xml:148: <public type="attr" name="contentPaddingBottom" id="0x7f020079" />
- resources/res/values/public.xml:172: <public type="attr" name="drawableBottomCompat" id="0x7f020091" />
- resources/res/values/public.xml:239: <public type="attr" name="lastBaselineToBottomHeight" id="0x7f0200d4" />
- resources/res/values/public.xml:249: <public type="attr" name="layout_constraintBottom_creator" id="0x7f0200de" />
- resources/res/values/public.xml:250: <public type="attr" name="layout_constraintBottom_toBottomOf" id="0x7f0200df" />

## Search hits in decoded resources
- Matching lines found: 111; displaying up to 40.
- drawable/abc_btn_colored_material.xml:2: <inset android:insetLeft="@dimen/abc_button_inset_horizontal_material" android:insetRight="@dimen/abc_button_inset_horizontal_material" android:insetTop="@dimen/abc_button_inset_vertical_material" ...
- drawable/abc_btn_colored_material.xml:11: <padding android:left="@dimen/abc_button_padding_horizontal_material" android:top="@dimen/abc_button_padding_vertical_material" android:right="@dimen/abc_button_padding_horizontal_material" android...
- drawable/abc_btn_colored_material.xml:18: <padding android:left="@dimen/abc_button_padding_horizontal_material" android:top="@dimen/abc_button_padding_vertical_material" android:right="@dimen/abc_button_padding_horizontal_material" android...
- drawable/abc_btn_default_mtrl_shape.xml:2: <inset android:insetLeft="@dimen/abc_button_inset_horizontal_material" android:insetRight="@dimen/abc_button_inset_horizontal_material" android:insetTop="@dimen/abc_button_inset_vertical_material" ...
- drawable/abc_btn_default_mtrl_shape.xml:7: <padding android:left="@dimen/abc_button_padding_horizontal_material" android:top="@dimen/abc_button_padding_vertical_material" android:right="@dimen/abc_button_padding_horizontal_material" android...
- drawable/abc_dialog_material_background.xml:2: <inset android:insetLeft="16.0dp" android:insetRight="16.0dp" android:insetTop="16.0dp" android:insetBottom="16.0dp"
- drawable/abc_edit_text_material.xml:2: <inset android:insetLeft="@dimen/abc_edit_text_inset_horizontal_material" android:insetRight="@dimen/abc_edit_text_inset_horizontal_material" android:insetTop="@dimen/abc_edit_text_inset_top_materi...
- drawable/abc_spinner_textfield_background_material.xml:2: <inset android:insetLeft="@dimen/abc_control_inset_material" android:insetRight="@dimen/abc_control_inset_material" android:insetTop="@dimen/abc_control_inset_material" android:insetBottom="@dimen/...
- drawable/common_google_signin_btn_icon_dark_focused.xml:4: <item android:left="1.0dp" android:top="1.0dp" android:right="1.0dp" android:bottom="1.0dp">
- drawable/common_google_signin_btn_icon_disabled.xml:4: <item android:left="3.0dp" android:top="3.0dp" android:right="3.0dp" android:bottom="3.0dp">
- drawable/common_google_signin_btn_icon_disabled.xml:8: <padding android:left="7.0dp" android:top="7.0dp" android:right="7.0dp" android:bottom="7.0dp" />
- drawable/common_google_signin_btn_icon_light_focused.xml:4: <item android:left="1.0dp" android:top="1.0dp" android:right="1.0dp" android:bottom="1.0dp">
- drawable/common_google_signin_btn_text_dark_focused.xml:4: <item android:left="1.0dp" android:top="1.0dp" android:right="1.0dp" android:bottom="1.0dp">
- drawable/common_google_signin_btn_text_disabled.xml:4: <item android:left="3.0dp" android:top="3.0dp" android:right="3.0dp" android:bottom="3.0dp">
- drawable/common_google_signin_btn_text_disabled.xml:8: <padding android:left="50.0dp" android:top="8.0dp" android:right="11.0dp" android:bottom="7.0dp" />
- drawable/common_google_signin_btn_text_light_focused.xml:4: <item android:left="1.0dp" android:top="1.0dp" android:right="1.0dp" android:bottom="1.0dp">
- drawable/notification_action_background.xml:5: <inset android:insetLeft="@dimen/compat_button_inset_horizontal_material" android:insetRight="@dimen/compat_button_inset_horizontal_material" android:insetTop="@dimen/compat_button_inset_vertical_m...
- drawable/notification_action_background.xml:9: <padding android:left="@dimen/compat_button_padding_horizontal_material" android:top="@dimen/compat_button_padding_vertical_material" android:right="@dimen/compat_button_padding_horizontal_material...
- drawable-watch/common_google_signin_btn_text_disabled.xml:4: <item android:left="3.0dp" android:top="3.0dp" android:right="3.0dp" android:bottom="3.0dp">
- drawable-watch/common_google_signin_btn_text_disabled.xml:7: <padding android:left="50.0dp" android:top="8.0dp" android:right="11.0dp" android:bottom="7.0dp" />
- layout/abc_action_menu_item_layout.xml:2: <androidx.appcompat.view.menu.ActionMenuItemView android:textAppearance="?actionMenuTextAppearance" android:textColor="?actionMenuTextColor" android:gravity="center" android:layout_gravity="center"...
- layout/abc_activity_chooser_view.xml:4: <FrameLayout android:layout_gravity="center" android:id="@id/expand_activities_button" android:background="?actionBarItemBackground" android:paddingLeft="12.0dp" android:paddingTop="2.0dp" android:...
- layout/abc_activity_chooser_view.xml:7: <FrameLayout android:layout_gravity="center" android:id="@id/default_activity_button" android:background="?actionBarItemBackground" android:paddingLeft="12.0dp" android:paddingTop="2.0dp" android:p...
- layout/abc_alert_dialog_button_bar_material.xml:2: <ScrollView android:id="@id/buttonPanel" android:layout_width="match_parent" android:layout_height="wrap_content" android:fillViewport="true" android:scrollIndicators="top|bottom" style="?buttonBar...
- layout/abc_alert_dialog_button_bar_material.xml:4: <androidx.appcompat.widget.ButtonBarLayout android:gravity="bottom" android:orientation="horizontal" android:paddingLeft="12.0dp" android:paddingTop="4.0dp" android:paddingRight="12.0dp" android:pa...
- layout/abc_alert_dialog_material.xml:14: <ImageView android:layout_gravity="bottom" android:id="@id/scrollIndicatorDown" android:background="#1f000000" android:visibility="gone" android:layout_width="match_parent" android:layout_height="1...
- layout/abc_cascading_menu_item_layout.xml:4: <ImageView android:id="@id/group_divider" android:background="@drawable/abc_list_divider_material" android:layout_width="match_parent" android:layout_height="1.0dp" android:layout_marginTop="4.0dp"...
- layout/abc_list_menu_item_icon.xml:2: <ImageView android:layout_gravity="center_vertical" android:id="@id/icon" android:duplicateParentState="true" android:layout_width="wrap_content" android:layout_height="wrap_content" android:layout...
- layout/abc_popup_menu_item_layout.xml:4: <ImageView android:id="@id/group_divider" android:background="@drawable/abc_list_divider_material" android:layout_width="match_parent" android:layout_height="1.0dp" android:layout_marginTop="4.0dp"...
- layout/abc_search_dropdown_item_icons_2line.xml:4: <ImageView android:id="@android:id/icon1" android:visibility="invisible" android:layout_width="@dimen/abc_dropdownitem_icon_width" android:layout_height="48.0dp" android:scaleType="centerInside" an...
- layout/abc_search_dropdown_item_icons_2line.xml:5: <ImageView android:id="@id/edit_query" android:background="?selectableItemBackground" android:visibility="gone" android:layout_width="48.0dp" android:layout_height="48.0dp" android:scaleType="cente...
- layout/abc_search_dropdown_item_icons_2line.xml:6: <ImageView android:id="@android:id/icon2" android:visibility="gone" android:layout_width="48.0dp" android:layout_height="48.0dp" android:scaleType="centerInside" android:layout_alignParentTop="true...
- layout/abc_search_dropdown_item_icons_2line.xml:7: <TextView android:textAppearance="?textAppearanceSearchResultSubtitle" android:gravity="top" android:id="@android:id/text2" android:paddingBottom="4.0dp" android:visibility="gone" android:layout_wi...
- layout/abc_search_view.xml:4: <TextView android:textAppearance="?android:textAppearanceMedium" android:textColor="?android:textColorPrimary" android:gravity="center_vertical" android:id="@id/search_badge" android:visibility="go...
- layout/abc_select_dialog_material.xml:2: <view android:layout_gravity="start" android:id="@id/select_dialog_listview" android:scrollbars="vertical" android:fadingEdge="none" android:clipToPadding="false" android:layout_width="match_parent...
- layout/abc_tooltip.xml:4: <TextView android:textAppearance="@style/TextAppearance.AppCompat.Tooltip" android:textColor="?tooltipForegroundColor" android:ellipsize="end" android:id="@id/message" android:background="?tooltipF...
- layout/expand_button.xml:5: <RelativeLayout android:paddingTop="16.0dp" android:paddingBottom="16.0dp" android:layout_width="0.0dp" android:layout_height="wrap_content" android:layout_weight="1.0">
- layout/image_frame.xml:2: <LinearLayout android:gravity="start|center" android:orientation="horizontal" android:id="@id/icon_frame" android:paddingLeft="0.0dp" android:paddingTop="4.0dp" android:paddingRight="8.0dp" android...
- layout/notification_template_big_media.xml:7: <LinearLayout android:orientation="horizontal" android:id="@id/media_actions" android:layout_width="match_parent" android:layout_height="48.0dp" android:layout_marginLeft="12.0dp" android:layout_ma...
- layout/notification_template_big_media_custom.xml:7: <FrameLayout android:id="@id/notification_main_column" android:layout_width="match_parent" android:layout_height="wrap_content" android:layout_marginLeft="@dimen/notification_content_margin_start" ...

## Search hits in selected native/IL2CPP strings
- Total matching printable strings: 710.
### assets/bin/Data/Managed/Metadata/global-metadata.dat
- )$WhiteIn$WhiteIn_1$WhiteOut$WhiteOut_1$__BindingManager--ClearAllBindings%% #% #-% -#%#%#-%)%-#%20%26%2C%3D%a%backspace%bannerid%%basepath%%c%d%down%f%left%right%s%subloop%%subloop0%%subloop00%%subloop000%%subloop000...
- -END-HERO-Infinity-_.!~*'()-bar-buildsrc-container-handle-image-inf-infinity-item-label-underline-unity-background-image-tint-color-unity-background-scale-mode-unity-editor-text-rendering-mode-unity-font-unity-font-de...
- {0}</color><color=grey><color=red><color=yAqua><color=yAqua><size=18><color=yParamorange><color=yPink><color=yellow>Capacity Over</color><color><color>{1,4}<count><define id='<easing-function>#<empty><filename unknown...
- AssignmentCharacter_001AssignmentCharacter_002AssignmentCharacter_003Async: AsyncGPUReadback cannot use Temp memory as input since the result may only become available at an unspecified point in the future.AsyncMiniJS...
- 4 BOOLEAN BWBackBackGradationLowerBackGradationUpperBackbufferBackgroundBackimgBad addressBad file numberBad indices/count arguments (bufferStartIndex:{0} count:{1} elementSize:{2}, this.count:{3}, this.stride{4})Bad ...
- : Common Language Runtime detected an invalid program.CompareInfoCompareInfo - CompareOption.Ordinal cannot be used with other options.ComparerCompiler error: Generated a subpass pass but no pass is currently active.C...
- : Draw.01DrawMeshInstanced is not supported.DrawMeshInstancedProcedural is not supported.DrawReactionIsDoneDrawingDeckDropdown (Legacy)Dropdown ListDropdown.valueDuckEndDuckStartDuckVolDuckingCategoryDue time too larg...
- : Guid should contain 32 digits with 4 dashes (xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx).Guid string should only contain hexadecimal characters.GuideCharaWidgetGuideLineHH:mmHBoxHDR Mode Change RequestedHDR Output ActiveH...
- : ImmediatePopImportedGraphicsBufferInIn a player, panel context type must be set to Player.InReplaceIncPanIncPitchIncSrcIncVolIncompatible Delegate Types. First is {0} second is {1}.Incompatible handle: Trying to ass...
- : OpaqueOpenOpenBannerOpenFloorOpenPackRootOpenPanelOpenRecommendListResultOpenRentalDeckOpenRewardListResultOpenUrlOpenedPacksOpenedPacks.dialogOpenedPacks.packOpenedPacks.packSROpenedPacks.packUROpenedPacks.recommen...
- ShaderDebugPrintManager.BufferReadCompleteShaderVariablesProbeVolumesShakeShakeXShakeYShaped Absolute Input MotionShared UI MeshSharing violationSharing violation on path {0}Shine1_1ShopShop.Lineup.topbanner.cworkShop...
- The path '{0}' is too long, or a component of the specified path is too long.The printf operation failedThe process cannot access the file '{0}' because it is being used by another process.The process cannot access th...
- sTwoPaneSplitView needs exactly 2 children.TypeType Type 'Type '{0}' in Assembly '{1}' is not marked as serializable.Type '{0}' of type '{1}' does not derive from System.ObjectType `Type and assembly attributes cannot...
- 06SYYAxisYDTAYGO_Card_NAYear must be between 1 and 9999.Year, Month, and Day parameters describe an un-representable DateTime.Years value must be between +/-10000.Ygom/BloomProcedureYgom/CustomColorMatrixYgom/DepthDra...
- ]\\"\((?<v>[^\(]*?)\)\.[^\.]*$\<\>\A[a-zA-Z0-9-._~]{1,100}\Z\[[0-9]+\]\\\\[\b\f\n\r\t\u\x{0:X2}\{0:D3}\{0:D}]] ] First character index: ] Last character index: ] MaxRange: '] Property=[] Units Per EM set to ] and Igno...
- {2}error_codeertacardnameeses-ESescapeetetc_tabetexteueuc-cneuc-jpeuc-krev0002_charagetev0002_opev0002_pegasuslv50ev0004_charagetev0004_zorcev0007_paradoxbrothers_lv50ev0014_maliklv50ev01ev02ev03ev_idev_noevaluateeval...
- {76}: {77}{0}: {1} precompiled chunk{0}: {1}, {2}: {3}{0}: {1}, {2}: {3}, {4}: {5}, {6}: {7}{0}: {1}/{2}{0}:{1}{0}:{1}: {0}:{1}: {2}{0}<{1}>{0}L/{1:D4}{0}_mrk{1:D6}{0}_rank_{1:D2}{0}_{1}{0}_{1}_{2}{0}_{1}x{2}{0}f{0}fl...
- bottomTargetOpt
- bottomcharaList
- bottomCheckedCharaList
### lib/arm64-v8a/libduel.so
- DLL_DuelGetDamageSrcPosition
- DLL_DuelGetDamageDstPosition
- DLL_DuelGetDamageValue
- DLL_DuelComCheatCard
### lib/arm64-v8a/libil2cpp.so
- UnityEngine.RectOffset::get_bottom_Injected(System.IntPtr)
- DLL_DuelGetDamageDstPosition
- DLL_DuelGetDamageSrcPosition
- UnityEngine.Rendering.CommandBuffer::SetInstanceMultiplier_Injected(System.IntPtr,System.UInt32)
- DLL_DuelGetDamageValue
- UnityEngine.ParticleSystem/MainModule::get_startDelayMultiplier()
- UnityEngine.RectOffset::set_bottom_Injected(System.IntPtr,System.Int32)
- UnityEngine.ParticleSystem/MainModule::get_startLifetimeMultiplier()
- Absurd stack bottom value
- UnityEngine.ParticleSystem/MainModule::set_startDelayMultiplier(System.Single)
- Tswana (Botswana)
- Botswana
- Botswanan Pula
- sobota
- subota
- Labotlhano
### lib/arm64-v8a/libplatinmods.so
- Java_com_platinmods_FloatingModMenuService_isGameLibLoaded
- Java_com_platinmods_FloatingModMenuService_Title
- Java_com_platinmods_FloatingModMenuService_Heading
- Java_com_platinmods_FloatingModMenuService_Icon
- Java_com_platinmods_FloatingModMenuService_IconWebViewData
- Java_com_platinmods_FloatingModMenuService_settingsList
- Java_com_platinmods_MainActivity_Toast
- Java_com_platinmods_FloatingModMenuService_getFeatureList
- Java_com_platinmods_Preferences_Changes
- _ZN8CryptoPP24Baseline_MultiplyBottom2EPmPKmS2_
- _ZN8CryptoPP24Baseline_MultiplyBottom4EPmPKmS2_
- _ZN8CryptoPP24Baseline_MultiplyBottom8EPmPKmS2_
- _ZN8CryptoPP25Baseline_MultiplyBottom16EPmPKmS2_
- _ZN8CryptoPP23RecursiveMultiplyBottomEPmS0_PKmS2_m
- _ZNK8CryptoPP7Integer21MultiplicativeInverseEv
- _ZTVN8CryptoPP12AbstractRingINS_7IntegerEE20MultiplicativeGroupTE
- _ZNK8CryptoPP24MontgomeryRepresentation21MultiplicativeInverseERKNS_7IntegerE
- _ZNK8CryptoPP17ModularArithmetic22MultiplicativeIdentityEv
- _ZNK8CryptoPP17ModularArithmetic21MultiplicativeInverseERKNS_7IntegerE
- _ZNK8CryptoPP24MontgomeryRepresentation22MultiplicativeIdentityEv
### lib/armeabi-v7a/libduel.so
- DLL_DuelGetDamageSrcPosition
- DLL_DuelGetDamageDstPosition
- DLL_DuelGetDamageValue
- DLL_DuelComCheatCard
### lib/armeabi-v7a/libil2cpp.so
- UnityEngine.RectOffset::get_bottom_Injected(System.IntPtr)
- DLL_DuelGetDamageDstPosition
- DLL_DuelGetDamageSrcPosition
- UnityEngine.Rendering.CommandBuffer::SetInstanceMultiplier_Injected(System.IntPtr,System.UInt32)
- DLL_DuelGetDamageValue
- UnityEngine.ParticleSystem/MainModule::get_startDelayMultiplier()
- UnityEngine.RectOffset::set_bottom_Injected(System.IntPtr,System.Int32)
- UnityEngine.ParticleSystem/MainModule::get_startLifetimeMultiplier()
- Absurd stack bottom value
- UnityEngine.ParticleSystem/MainModule::set_startDelayMultiplier(System.Single)
- Tswana (Botswana)
- Botswana
- Botswanan Pula
- sobota
- subota
- Labotlhano
### lib/armeabi-v7a/libplatinmods.so
- Java_com_platinmods_FloatingModMenuService_isGameLibLoaded
- Java_com_platinmods_FloatingModMenuService_Title
- Java_com_platinmods_FloatingModMenuService_Heading
- Java_com_platinmods_FloatingModMenuService_Icon
- Java_com_platinmods_FloatingModMenuService_IconWebViewData
- Java_com_platinmods_FloatingModMenuService_settingsList
- Java_com_platinmods_MainActivity_Toast
- Java_com_platinmods_FloatingModMenuService_getFeatureList
- Java_com_platinmods_Preferences_Changes
- _ZN8CryptoPP24Baseline_MultiplyBottom2EPjPKjS2_
- _ZN8CryptoPP24Baseline_MultiplyBottom8EPjPKjS2_
- _ZN8CryptoPP24Baseline_MultiplyBottom4EPjPKjS2_
- _ZN8CryptoPP25Baseline_MultiplyBottom16EPjPKjS2_
- _ZN8CryptoPP23RecursiveMultiplyBottomEPjS0_PKjS2_j
- _ZNK8CryptoPP7Integer21MultiplicativeInverseEv
- _ZTVN8CryptoPP12AbstractRingINS_7IntegerEE20MultiplicativeGroupTE
- _ZNK8CryptoPP24MontgomeryRepresentation21MultiplicativeInverseERKNS_7IntegerE
- _ZNK8CryptoPP17ModularArithmetic22MultiplicativeIdentityEv
- _ZNK8CryptoPP17ModularArithmetic21MultiplicativeInverseERKNS_7IntegerE
- _ZNK8CryptoPP24MontgomeryRepresentation22MultiplicativeIdentityEv

## Interpretation guardrails
- Exact string hits locate potential code/resources; they do not prove event wiring, control flow, or that a menu toggle works.
- JADX primarily analyzes DEX/Java/Kotlin code. Unity IL2CPP game logic may be compiled into native libraries and metadata; full native tracing requires separate tooling and careful symbol/metadata analysis.
- Static decompilation does not prove server-authoritative behavior, online compatibility, or runtime success.
- The APK was not executed or installed. Temporary decompiled source was not committed to the repository.

## Recommended next step
Review the source/resource/native-string hits together with the decompiled manifest. Record exact file/class/method evidence for each feature in MOD_CANDIDATES.md, then separate code-reading hypotheses from any isolated test results.

