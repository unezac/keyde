# 🧪 Quick API Testing Guide

## Run These Tests After Starting the App

### Step 1: Start Backend & Frontend
```powershell
# Terminal 1: Backend
cd D:\CODEcopilot\KeyGermany.de
python -m uvicorn backend.app.main:app --reload --host 127.0.0.1 --port 8000

# Terminal 2: Frontend
cd D:\CODEcopilot\KeyGermany.de\frontend
python -m http.server 3000
```

---

## Test 1: Health Check ✅

**Command:**
```bash
curl http://127.0.0.1:8000/api/health
```

**Expected Output:**
```json
{"status":"ok","service":"KeyGermany API"}
```

**Status:** ✅ If you see this, backend is running!

---

## Test 2: Get Random Sentence 📝

**Command:**
```bash
curl "http://127.0.0.1:8000/api/sentences/random"
```

**Expected Output:**
```json
{
  "id": 1,
  "german_text": "Der schnelle braune Fuchs springt über den faulen Hund.",
  "english_translation": "The quick brown fox jumps over the lazy dog.",
  "arabic_translation": "الثعلب البني السريع يقفز فوق الكلب الكسول.",
  "level": "B2",
  "difficulty_score": 5,
  "category": "Daily Life",
  "created_at": "2026-04-30T...",
  "updated_at": "2026-04-30T..."
}
```

**Status:** ✅ Database is loaded and API works!

---

## Test 3: Filter by Level 🎯

**Command:**
```bash
curl "http://127.0.0.1:8000/api/sentences/random?level=B2"
```

**Expected:** Sentence with `"level": "B2"`

---

## Test 4: Filter by Category 📂

**Command:**
```bash
curl "http://127.0.0.1:8000/api/sentences/random?category=Daily%20Life"
```

**Expected:** Sentence with `"category": "Daily Life"`

---

## Test 5: Get All Sentences 📚

**Command:**
```bash
curl "http://127.0.0.1:8000/api/sentences?level=B2&limit=3"
```

**Expected Output:** Array of 3 sentences (or fewer if not enough in DB)
```json
[
  { "id": 1, "german_text": "...", ... },
  { "id": 2, "german_text": "...", ... },
  { "id": 3, "german_text": "...", ... }
]
```

---

## Test 6: Get Categories 📋

**Command:**
```bash
curl http://127.0.0.1:8000/api/categories
```

**Expected Output:**
```json
["Daily Life", "Food & Drinks", "Education"]
```

---

## Test 7: Get Levels 🎚️

**Command:**
```bash
curl http://127.0.0.1:8000/api/levels
```

**Expected Output:**
```json
["B2"]
```
(Or multiple levels if more data in DB)

---

## Test 8: Frontend Integration 🌐

1. Open http://127.0.0.1:3000 in browser
2. Open **Developer Console** (F12 → Console tab)
3. Copy & paste this test:

```javascript
// Test API connection
const API_BASE_URL = 'http://127.0.0.1:8000/api';

console.log('🧪 Testing API Integration...\n');

// Test 1: Health
fetch(`${API_BASE_URL}/health`)
  .then(r => r.json())
  .then(d => console.log('✅ Health Check:', d))
  .catch(e => console.error('❌ Health Check Failed:', e));

// Test 2: Random Sentence
fetch(`${API_BASE_URL}/sentences/random?level=B2`)
  .then(r => r.json())
  .then(d => {
    console.log('✅ Random Sentence:', d);
    
    // Test normalization
    const normalized = {
      id: d.id,
      german: d.german_text,
      en: d.english_translation,
      ar: d.arabic_translation,
      level: d.level
    };
    console.log('✅ Normalized Format:', normalized);
  })
  .catch(e => console.error('❌ Random Sentence Failed:', e));

// Test 3: Categories
fetch(`${API_BASE_URL}/categories`)
  .then(r => r.json())
  .then(d => console.log('✅ Categories:', d))
  .catch(e => console.error('❌ Categories Failed:', e));
```

**Expected Console Output:**
```
🧪 Testing API Integration...

✅ Health Check: {status: "ok", service: "KeyGermany API"}
✅ Random Sentence: {id: 1, german_text: "...", ...}
✅ Normalized Format: {id: 1, german: "...", en: "...", ar: "...", level: "B2"}
✅ Categories: ["Daily Life", "Food & Drinks", "Education"]
```

---

## Test 9: Frontend UI Test 🎮

1. Go to http://127.0.0.1:3000
2. Check:
   - [ ] German sentence displays
   - [ ] English/Arabic translation shows below
   - [ ] Typing input works
   - [ ] Keyboard highlights as you type
   - [ ] Progress bar fills as you type
   - [ ] Changes level → new sentence loads
   - [ ] Changes category → filters work
   - [ ] "Listen" button plays German
   - [ ] Complete sentence → auto-advances

---

## ❌ Troubleshooting

### "Connection refused"
```
Frontend can't reach backend on port 8000
→ Check backend is running
→ Run: python -m uvicorn backend.app.main:app --reload --host 127.0.0.1 --port 8000
```

### "404 Not Found"
```
API endpoint doesn't exist
→ Check endpoint URL is correct
→ Backend routes registered? Check: ✅ Confirmed all routes exist
```

### "No sentences found"
```
Database is empty
→ Delete keygermany.db and restart backend
→ Automatic seeding will populate sample data
```

### "CORS error in browser"
```
Frontend blocked by backend CORS policy
→ Backend has CORSMiddleware enabled
→ Should NOT see this error if backend is working
→ Clear browser cache and try again
```

### "Typing doesn't validate"
```
Frontend receiving wrong field names from API
→ Check normalizeApiSentence() is being called
→ API response should have: german_text, english_translation, arabic_translation
→ Frontend should map to: german, en, ar
```

---

## 🎯 Quick Status Check

Run this single command to test everything:

```powershell
# Tests all endpoints in sequence
$endpoints = @(
    'health',
    'sentences/random',
    'sentences',
    'categories',
    'levels'
)

$endpoints | ForEach-Object {
    Write-Host "`n✅ Testing: /api/$_"
    Invoke-WebRequest -Uri "http://127.0.0.1:8000/api/$_" | Select-Object -ExpandProperty Content | ConvertFrom-Json | ConvertTo-Json -Depth 2 | Write-Host
}
```

---

## ✅ Final Checklist

- [ ] Backend runs without errors
- [ ] Frontend loads without errors
- [ ] All 6 API endpoints respond correctly
- [ ] Frontend displays sentences from API
- [ ] Typing validation works
- [ ] Level/category filters work
- [ ] Browser console shows no errors
- [ ] Statistics save correctly

**If all checks pass: ✅ API Integration is Perfect! 🎉**

---

Generated: 2026-04-30
