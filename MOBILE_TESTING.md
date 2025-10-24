# Mobile Testing Guide

## Quick Start Testing

### Testing on Your Mobile Device

#### Option 1: Local Network (Fastest)

1. **Start the server**:
   ```bash
   python server.py
   ```

2. **Find your network IP** (displayed in terminal output):
   ```
   🎯 Access the game at:
      • Local:    http://localhost:2025
      • Network:  http://192.168.1.XXX:2025
   ```

3. **On your mobile device**:
   - Connect to the **same WiFi network** as your computer
   - Open browser (Safari on iPhone, Chrome on Android)
   - Navigate to: `http://YOUR_IP:2025`
   - Example: `http://192.168.1.100:2025`

4. **Test features**:
   - ✅ Canvas adapts to screen size
   - ✅ Touch buttons appear and work
   - ✅ Swipe gestures control snake
   - ✅ Rotate device (portrait/landscape works)
   - ✅ No accidental zoom or scroll

#### Option 2: ngrok (Remote Testing)

1. **Install ngrok**:
   ```bash
   # Download from https://ngrok.com/download
   # Or use: brew install ngrok (Mac)
   ```

2. **Start server** (terminal 1):
   ```bash
   python server.py
   ```

3. **Start ngrok** (terminal 2):
   ```bash
   ngrok http 2025
   ```

4. **Use ngrok URL**:
   - Copy the `https://xxxx.ngrok.io` URL
   - Open on ANY device (anywhere in the world)
   - Test all mobile features

---

## Device-Specific Testing

### iPhone Testing

**Safari iOS** (Recommended):

1. Open Safari
2. Navigate to server URL
3. Test touch controls
4. Test PWA install:
   - Tap Share button (square with arrow)
   - Tap "Add to Home Screen"
   - Open app from home screen
   - Verify standalone mode (no Safari UI)

**Check**:
- ✅ Touch buttons visible below canvas
- ✅ Swipe gestures work in all 4 directions
- ✅ No horizontal scrolling
- ✅ Safe area respected (no notch interference)
- ✅ Landscape mode works
- ✅ Game continues after rotation

**iPhone Models to Test**:
- iPhone SE (small screen)
- iPhone 12/13/14 (notched)
- iPhone Pro Max (large screen)
- iPad (tablet size)

### Android Testing

**Chrome Mobile** (Recommended):

1. Open Chrome
2. Navigate to server URL
3. Test touch controls
4. Test PWA install:
   - Tap menu (3 dots)
   - Tap "Add to Home screen"
   - Or wait for install banner
   - Open app from home screen

**Samsung Internet**:
- Test same features
- Verify theme color in task switcher

**Check**:
- ✅ Touch buttons visible
- ✅ Swipe gestures responsive
- ✅ Theme color applied
- ✅ Install banner appears
- ✅ Orientation changes smooth
- ✅ Back button behavior acceptable

---

## Feature Testing Checklist

### Touch Controls

**On-Screen Buttons**:
- [ ] Tap Up arrow → snake moves up
- [ ] Tap Down arrow → snake moves down
- [ ] Tap Left arrow → snake moves left
- [ ] Tap Right arrow → snake moves right
- [ ] Visual feedback on tap (button scales)
- [ ] No delay in response (<100ms feel)
- [ ] Buttons hidden on desktop (>768px)

**Swipe Gestures**:
- [ ] Swipe up → snake moves up
- [ ] Swipe down → snake moves down
- [ ] Swipe left → snake moves left
- [ ] Swipe right → snake moves right
- [ ] Diagonal swipes register correctly
- [ ] Short swipes ignored (prevents accidents)
- [ ] Swipes work anywhere on canvas

### Responsive Design

**Portrait Mode**:
- [ ] Canvas fits screen width
- [ ] All UI elements visible
- [ ] No horizontal scrolling
- [ ] Touch buttons below canvas
- [ ] Score board readable
- [ ] Buttons minimum 44x44px

**Landscape Mode**:
- [ ] Canvas resizes appropriately
- [ ] Game state preserved
- [ ] No layout shift
- [ ] All controls accessible
- [ ] Performance maintained

**Screen Sizes**:
- [ ] Small phone (320px): Canvas ~280px
- [ ] Medium phone (375px): Canvas ~335px
- [ ] Large phone (414px): Canvas ~374px
- [ ] Tablet (768px): Canvas ~560px
- [ ] Desktop (>1024px): Canvas 600px max

### PWA Features

**Installation**:
- [ ] Manifest loads correctly
- [ ] App icon displays
- [ ] Install prompt appears (Android)
- [ ] Manual install works (iOS/Android)
- [ ] App opens in standalone mode
- [ ] No browser UI visible

**Standalone Mode**:
- [ ] Theme color applied to status bar
- [ ] Safe areas respected
- [ ] App title shown correctly
- [ ] Back button behavior (Android)
- [ ] Splash screen displays (optional)

### Performance

**Frame Rate**:
- [ ] Smooth 60 FPS on idle
- [ ] 50-60 FPS during gameplay
- [ ] No stuttering during swipes
- [ ] Orientation change <200ms
- [ ] Canvas resize smooth

**Touch Response**:
- [ ] Button tap <50ms delay
- [ ] Swipe recognized <100ms
- [ ] No missed inputs
- [ ] No double-tap zoom
- [ ] No accidental scrolling

### Accessibility

**Touch Targets**:
- [ ] Buttons ≥44x44px (iOS guideline)
- [ ] Buttons ≥48x48px (Android guideline)
- [ ] Adequate spacing between buttons
- [ ] Large tap areas

**Visual**:
- [ ] Text readable at 16px+
- [ ] High contrast (4.5:1+)
- [ ] No text truncation
- [ ] Colors distinguishable

**Screen Reader** (Optional):
- [ ] ARIA labels present
- [ ] Buttons describable
- [ ] Semantic HTML structure

---

## Browser DevTools Mobile Simulation

### Chrome DevTools

1. Open DevTools (F12)
2. Click device toggle (Ctrl+Shift+M)
3. Select device:
   - iPhone SE (375x667)
   - iPhone 12 Pro (390x844)
   - iPad (768x1024)
   - Galaxy S20 (360x800)

4. Test features:
   - Responsive canvas
   - Touch controls (click on buttons)
   - Orientation toggle
   - Safe area simulation

**Limitations**:
- Swipe gestures don't work perfectly
- Can't test actual touch feel
- No real PWA install

**Recommendation**: Use for quick checks, test on real devices for accuracy

---

## Common Issues & Fixes

### Issue: Touch Buttons Not Appearing

**Debug**:
1. Open browser console (desktop)
2. Simulate mobile viewport
3. Check console for errors
4. Verify CSS media query: `@media (min-width: 768px)`

**Fix**:
- Buttons should be hidden >768px
- Visible <768px

### Issue: Swipes Not Working

**Debug**:
1. Check if `touchstart` and `touchend` events fire
2. Verify `minSwipeDistance` (default 30px)
3. Test with longer swipes

**Fix**:
```javascript
const minSwipeDistance = 20; // Reduce from 30
```

### Issue: Canvas Too Small

**Debug**:
1. Check screen width in console: `window.innerWidth`
2. Check canvas size: `canvas.width`
3. Verify calculation in `resizeCanvas()`

**Fix**:
```javascript
const maxSize = Math.min(
    window.innerWidth - 20,  // Reduce padding
    window.innerHeight - 300, // Reduce header space
    600
);
```

### Issue: Layout Shifts on Rotate

**Debug**:
1. Rotate device slowly
2. Watch for canvas size change
3. Check if `orientationchange` fires

**Fix**: Already implemented with 100ms delay

### Issue: Game Behind Notch (iPhone X+)

**Debug**:
1. Check safe area insets
2. Verify `viewport-fit=cover`
3. Check CSS: `env(safe-area-inset-*)`

**Fix**: Already implemented in body padding

---

## Performance Testing

### FPS Monitoring

Add to console:
```javascript
let frames = 0;
let lastTime = performance.now();
setInterval(() => {
    const now = performance.now();
    const fps = frames / ((now - lastTime) / 1000);
    console.log(`FPS: ${fps.toFixed(1)}`);
    frames = 0;
    lastTime = now;
}, 1000);
```

**Target**: 55-60 FPS

### Touch Latency Test

```javascript
canvas.addEventListener('touchstart', () => {
    console.time('touch-response');
});
// In changeDirection():
console.timeEnd('touch-response');
```

**Target**: <50ms

---

## Production Testing

### Before Launch Checklist

**Functionality**:
- [ ] All controls work on iOS Safari
- [ ] All controls work on Chrome Mobile
- [ ] PWA installs successfully
- [ ] Offline mode works (if service worker added)
- [ ] High scores persist
- [ ] No console errors

**Performance**:
- [ ] 60 FPS on iPhone 12+
- [ ] 60 FPS on mid-range Android
- [ ] Touch response <100ms
- [ ] Orientation change smooth
- [ ] No memory leaks (long session test)

**Compatibility**:
- [ ] iOS 14+ Safari
- [ ] Android Chrome 90+
- [ ] Samsung Internet
- [ ] Desktop browsers

**UX**:
- [ ] No accidental zoom
- [ ] No scroll bounce
- [ ] Touch targets adequate
- [ ] Visual feedback clear
- [ ] Instructions clear

---

## Automated Testing (Optional)

### Playwright Mobile Testing

```javascript
// test/mobile.spec.js
const { test, devices } = require('@playwright/test');

test.describe('Mobile Snake Game', () => {
    test.use(devices['iPhone 12']);

    test('loads on iPhone', async ({ page }) => {
        await page.goto('http://localhost:2025');
        const canvas = await page.locator('#gameCanvas');
        await expect(canvas).toBeVisible();
    });

    test('touch buttons appear', async ({ page }) => {
        await page.goto('http://localhost:2025');
        const upBtn = await page.locator('#btnUp');
        await expect(upBtn).toBeVisible();
    });
});
```

---

## Conclusion

**Minimum Testing Required**:
1. Test on at least one iPhone (Safari)
2. Test on at least one Android (Chrome)
3. Test portrait and landscape
4. Verify touch controls work
5. Confirm PWA installs

**Recommended Extended Testing**:
- Multiple iPhone models (SE, 12, Pro Max)
- Multiple Android devices (various sizes)
- Tablet testing (iPad, Android tablet)
- Performance profiling
- Battery usage monitoring

**Result**: Confident mobile deployment with proven cross-device compatibility.

---

**Last Updated**: October 24, 2025
