# Installing La Clef on your phone

La Clef is a **Progressive Web App (PWA)**. That means it can install onto your phone's home screen right from the browser — its own icon, fullscreen, works offline — with no app store, no account, and no cost.

You need an `https://` link first. The easiest way is the free **GitHub Pages** hosting described in [PUSH-TO-GITHUB.md](PUSH-TO-GITHUB.md). Once your app is live at something like:

```
https://YOUR-USERNAME.github.io/REPO-NAME/app/la-clef.html
```

…open that link on your phone and follow the steps below.

---

## Android (Chrome)

1. Open the link in **Chrome**.
2. You'll often see an **"Add to Home screen" / "Install"** banner — tap it.
3. If not, tap the **⋮ menu** (top right) → **Add to Home screen** → **Install**.
4. The La Clef icon (the fighter) appears on your home screen. Open it — it runs fullscreen, no browser bars, and works offline.

## iPhone / iPad (Safari)

1. Open the link in **Safari** (this only works in Safari, not Chrome on iOS).
2. Tap the **Share** button (the square with the up arrow).
3. Scroll down and tap **Add to Home Screen**.
4. Tap **Add**. The icon appears on your home screen and opens fullscreen.

---

## What works offline once installed

- Reading all lessons, exercises (hide/reveal), the sentence chips
- Voice (read-aloud and speak-to-answer)
- Themes and the fighter / XP / progress

The **live AI tutor** still needs a network connection and a backend (see the main README) — everything else runs without internet.

---

## If you want a real Android APK later

A home-screen PWA covers most needs, but if you specifically want an installable `.apk` (to sideload or put on the Play Store), the app can be wrapped with **[Capacitor](https://capacitorjs.com)**:

1. `npm init`, then `npm install @capacitor/core @capacitor/cli @capacitor/android`
2. `npx cap init` and point the web directory at the `app/` folder
3. `npx cap add android`
4. `npx cap open android` to open it in **Android Studio**, then Build → Build APK.

You don't need a paid account just to build an APK for your own phone. Putting it on the **Play Store** needs a one-time **$25** Google developer account.

**iOS native** (a true App Store app) requires a **Mac with Xcode** and a **$99/year** Apple Developer account — Apple's build tools only run on macOS. For iPhone, the Safari "Add to Home Screen" route above is the free, no-Mac option.
