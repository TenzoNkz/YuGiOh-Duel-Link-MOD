package com.chatgptmod.menu;

import android.app.Activity;
import android.content.Context;
import android.content.SharedPreferences;
import android.graphics.Color;
import android.graphics.drawable.GradientDrawable;
import android.view.Gravity;
import android.view.MotionEvent;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;
import android.widget.CheckBox;
import android.widget.FrameLayout;
import android.widget.LinearLayout;
import android.widget.TextView;

/**
 * Standalone, game-action-free CHATGPT MOD menu shell.
 *
 * This helper is injected into the original APK only by the separately reviewed
 * patch pipeline. It intentionally contains no IL2CPP calls, native hooks, or
 * gameplay actions. All persistent values live in an independent preferences
 * namespace.
 */
public final class ModMenu {
    private static final String TAG_ROOT = "com.chatgptmod.menu.ROOT";
    private static final String PREFS = "chatgpt_mod_local_ui";
    private static final String KEY_OPEN_ON_LAUNCH = "panel_open_on_launch";

    private ModMenu() {
    }

    public static void install(Activity activity) {
        if (activity == null) {
            return;
        }
        try {
            View contentView = activity.findViewById(android.R.id.content);
            if (!(contentView instanceof ViewGroup)) {
                return;
            }
            final ViewGroup content = (ViewGroup) contentView;
            if (content.findViewWithTag(TAG_ROOT) != null) {
                return;
            }

            final SharedPreferences preferences =
                    activity.getSharedPreferences(PREFS, Context.MODE_PRIVATE);
            final FrameLayout root = new FrameLayout(activity);
            root.setTag(TAG_ROOT);
            root.setBackgroundColor(Color.TRANSPARENT);
            root.setClickable(false);
            root.setFocusable(false);
            root.setClipChildren(false);
            root.setClipToPadding(false);

            FrameLayout.LayoutParams rootParams = new FrameLayout.LayoutParams(
                    ViewGroup.LayoutParams.MATCH_PARENT,
                    ViewGroup.LayoutParams.MATCH_PARENT);
            content.addView(root, rootParams);

            final LinearLayout panel = new LinearLayout(activity);
            panel.setOrientation(LinearLayout.VERTICAL);
            panel.setPadding(dp(activity, 16), dp(activity, 12),
                    dp(activity, 16), dp(activity, 12));
            panel.setBackground(panelBackground(activity));
            panel.setElevation(dp(activity, 8));
            panel.setVisibility(preferences.getBoolean(KEY_OPEN_ON_LAUNCH, false)
                    ? View.VISIBLE : View.GONE);

            FrameLayout.LayoutParams panelParams = new FrameLayout.LayoutParams(
                    dp(activity, 276),
                    ViewGroup.LayoutParams.WRAP_CONTENT,
                    Gravity.TOP | Gravity.END);
            panelParams.setMargins(0, dp(activity, 76), dp(activity, 8), 0);
            root.addView(panel, panelParams);

            TextView title = new TextView(activity);
            title.setText("CHATGPT MOD");
            title.setTextColor(Color.WHITE);
            title.setTextSize(18);
            title.setTypeface(null, android.graphics.Typeface.BOLD);
            panel.addView(title, new LinearLayout.LayoutParams(
                    ViewGroup.LayoutParams.MATCH_PARENT,
                    ViewGroup.LayoutParams.WRAP_CONTENT));

            TextView description = new TextView(activity);
            description.setText("Local menu settings");
            description.setTextColor(0xFFD4DCE8);
            description.setTextSize(12);
            LinearLayout.LayoutParams descriptionParams =
                    new LinearLayout.LayoutParams(
                            ViewGroup.LayoutParams.MATCH_PARENT,
                            ViewGroup.LayoutParams.WRAP_CONTENT);
            descriptionParams.topMargin = dp(activity, 4);
            panel.addView(description, descriptionParams);

            CheckBox openOnLaunch = new CheckBox(activity);
            openOnLaunch.setText("Keep panel open after restart");
            openOnLaunch.setTextColor(Color.WHITE);
            openOnLaunch.setTextSize(13);
            openOnLaunch.setButtonTintList(android.content.res.ColorStateList.valueOf(0xFF83C5FF));
            openOnLaunch.setChecked(preferences.getBoolean(KEY_OPEN_ON_LAUNCH, false));
            LinearLayout.LayoutParams checkParams = new LinearLayout.LayoutParams(
                    ViewGroup.LayoutParams.MATCH_PARENT,
                    ViewGroup.LayoutParams.WRAP_CONTENT);
            checkParams.topMargin = dp(activity, 8);
            panel.addView(openOnLaunch, checkParams);

            TextView note = new TextView(activity);
            note.setText("UI-only prototype. No gameplay actions are connected.");
            note.setTextColor(0xFFB8C2D1);
            note.setTextSize(11);
            LinearLayout.LayoutParams noteParams = new LinearLayout.LayoutParams(
                    ViewGroup.LayoutParams.MATCH_PARENT,
                    ViewGroup.LayoutParams.WRAP_CONTENT);
            noteParams.topMargin = dp(activity, 4);
            panel.addView(note, noteParams);

            final Button close = new Button(activity);
            close.setText("Close");
            close.setAllCaps(false);
            LinearLayout.LayoutParams closeParams = new LinearLayout.LayoutParams(
                    ViewGroup.LayoutParams.WRAP_CONTENT,
                    dp(activity, 40));
            closeParams.gravity = Gravity.END;
            closeParams.topMargin = dp(activity, 8);
            panel.addView(close, closeParams);

            openOnLaunch.setOnCheckedChangeListener((button, checked) ->
                    preferences.edit().putBoolean(KEY_OPEN_ON_LAUNCH, checked).apply());
            close.setOnClickListener(view -> panel.setVisibility(View.GONE));

            final Button launcher = new Button(activity);
            launcher.setText("CHATGPT MOD");
            launcher.setAllCaps(false);
            launcher.setTextSize(12);
            launcher.setTextColor(Color.WHITE);
            launcher.setPadding(dp(activity, 12), 0, dp(activity, 12), 0);
            launcher.setBackground(launcherBackground(activity));
            launcher.setElevation(dp(activity, 8));

            FrameLayout.LayoutParams launcherParams = new FrameLayout.LayoutParams(
                    ViewGroup.LayoutParams.WRAP_CONTENT,
                    dp(activity, 44),
                    Gravity.TOP | Gravity.END);
            launcherParams.setMargins(0, dp(activity, 20), dp(activity, 8), 0);
            root.addView(launcher, launcherParams);

            launcher.setOnClickListener(view -> panel.setVisibility(
                    panel.getVisibility() == View.VISIBLE ? View.GONE : View.VISIBLE));
            launcher.setOnTouchListener(new DragTouchListener());

            root.bringChildToFront(launcher);
        } catch (Throwable failure) {
            // A UI-helper failure must not prevent the original game Activity from launching.
            android.util.Log.e("CHATGPT_MOD", "Menu initialization failed", failure);
        }
    }

    private static GradientDrawable panelBackground(Activity activity) {
        GradientDrawable drawable = new GradientDrawable();
        drawable.setColor(0xF01B2432);
        drawable.setCornerRadius(dp(activity, 14));
        drawable.setStroke(dp(activity, 1), 0xFF53657B);
        return drawable;
    }

    private static GradientDrawable launcherBackground(Activity activity) {
        GradientDrawable drawable = new GradientDrawable();
        drawable.setColor(0xF0274262);
        drawable.setCornerRadius(dp(activity, 22));
        drawable.setStroke(dp(activity, 1), 0xFF80BFFF);
        return drawable;
    }

    private static int dp(Context context, int value) {
        return Math.round(value * context.getResources().getDisplayMetrics().density);
    }

    private static final class DragTouchListener implements View.OnTouchListener {
        private float downRawX;
        private float downRawY;
        private float startX;
        private float startY;
        private boolean moved;

        @Override
        public boolean onTouch(View view, MotionEvent event) {
            switch (event.getActionMasked()) {
                case MotionEvent.ACTION_DOWN:
                    downRawX = event.getRawX();
                    downRawY = event.getRawY();
                    startX = view.getX();
                    startY = view.getY();
                    moved = false;
                    return true;
                case MotionEvent.ACTION_MOVE:
                    float dx = event.getRawX() - downRawX;
                    float dy = event.getRawY() - downRawY;
                    if (!moved && Math.max(Math.abs(dx), Math.abs(dy)) > 6.0f) {
                        moved = true;
                    }
                    if (moved) {
                        ViewGroup parent = view.getParent() instanceof ViewGroup
                                ? (ViewGroup) view.getParent() : null;
                        float targetX = startX + dx;
                        float targetY = startY + dy;
                        if (parent != null) {
                            targetX = Math.max(0.0f, Math.min(targetX,
                                    Math.max(0.0f, parent.getWidth() - view.getWidth())));
                            targetY = Math.max(0.0f, Math.min(targetY,
                                    Math.max(0.0f, parent.getHeight() - view.getHeight())));
                        }
                        view.setX(targetX);
                        view.setY(targetY);
                    }
                    return true;
                case MotionEvent.ACTION_UP:
                    if (!moved) {
                        view.performClick();
                    }
                    return true;
                case MotionEvent.ACTION_CANCEL:
                    return true;
                default:
                    return false;
            }
        }
    }
}
