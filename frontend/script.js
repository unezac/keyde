const API_BASE_URL = 'http://127.0.0.1:8000/api';

const fallbackSentences = [
    {
        german: 'Ich bin glücklich, weil ich viel zu tun habe.',
        en: 'I am happy because I have a lot to do.',
        ar: 'أنا سعيد لأن لدي الكثير لأفعله.'
    },
    {
        german: 'Je mehr ich übe, desto sicherer schreibe ich auf Deutsch.',
        en: 'The more I practice, the more confidently I write in German.',
        ar: 'كلما تدربت أكثر، كتبت باللغة الألمانية بثقة أكبر.'
    },
    {
        german: 'Obwohl der Satz lang ist, tippe ich ihn Schritt für Schritt.',
        en: 'Although the sentence is long, I type it step by step.',
        ar: 'رغم أن الجملة طويلة، أكتبها خطوة بخطوة.'
    }
];

// Keyboard layout mappings
const keyboardLayouts = {
    qwertz: { name: 'QWERTZ', lang: 'de' },
    qwerty: { name: 'QWERTY', lang: 'en' },
    azerty: { name: 'AZERTY', lang: 'fr' }
};

// Achievements definition
const achievements = [
    { id: 'first_session', name: 'First Steps', description: 'Complete your first typing session', icon: '🌱' },
    { id: 'ten_sessions', name: 'Dedicated', description: 'Complete 10 typing sessions', icon: '🔥' },
    { id: 'fifty_sessions', name: 'Master', description: 'Complete 50 typing sessions', icon: '👑' },
    { id: 'perfect_accuracy', name: 'Perfect!', description: 'Achieve 100% accuracy in a session', icon: '⭐' },
    { id: 'speed_demon', name: 'Speed Demon', description: 'Reach 60 WPM or higher', icon: '⚡' },
    { id: 'five_hundred_words', name: 'Prolific', description: 'Type 500+ total words', icon: '📚' },
    { id: 'all_levels', name: 'Polyglot', description: 'Practice all difficulty levels', icon: '🌍' },
    { id: 'ten_favorites', name: 'Collector', description: 'Bookmark 10 sentences', icon: '❤️' },
    { id: 'streak_five', name: 'On Fire!', description: 'Complete 5 sessions without errors', icon: '🔥🔥' }
];

const sentenceDisplay = document.getElementById('sentence-display');
const translationDisplay = document.getElementById('translation-display');
const typingInput = document.getElementById('typing-input');
const progressBar = document.getElementById('progress-bar');
const progressLabel = document.getElementById('progress-label');
const accuracyLabel = document.getElementById('accuracy');
const nextKeyLabel = document.getElementById('next-key');
const wpmLabel = document.getElementById('wpm-label');
const typingState = document.getElementById('typing-state');
const levelDisplay = document.getElementById('level-display');
const favoriteButton = document.getElementById('favorite-button');
const keyboardKeys = [...document.querySelectorAll('.key[data-key]')];
const settingsToggle = document.getElementById('settings-toggle');
const settingsClose = document.getElementById('settings-close');
const settingsPanel = document.getElementById('settings-panel');
const statsToggle = document.getElementById('stats-toggle');
const statsClose = document.getElementById('stats-close');
const statsPanel = document.getElementById('stats-panel');
const statsReset = document.getElementById('stats-reset');
const achievementsToggle = document.getElementById('achievements-toggle');
const achievementsClose = document.getElementById('achievements-close');
const achievementsPanel = document.getElementById('achievements-panel');
const achievementsList = document.getElementById('achievements-list');
const keyboardLayoutSelect = document.getElementById('keyboard-layout-select');
const levelSelect = document.getElementById('level-select');
const categorySelect = document.getElementById('category-select');
const filterSelect = document.getElementById('filter-select');
const themeSelect = document.getElementById('theme-select');
const translationSelect = document.getElementById('translation-select');
const voiceSelect = document.getElementById('voice-select');
const germanVoiceSelect = document.getElementById('german-voice-select');
const voiceStyleSelect = document.getElementById('voice-style-select');
const keyboardSoundSelect = document.getElementById('keyboard-sound-select');
const listenButton = document.getElementById('listen-button');
const quickListenButton = document.getElementById('quick-listen-button');
const retryButton = document.getElementById('retry-button');
const skipButton = document.getElementById('skip-button');
const searchForm = document.getElementById('search-form');
const sentenceSearch = document.getElementById('sentence-search');

let sentenceBank = [...fallbackSentences];
let currentSentence = sentenceBank[0];
let isComplete = false;
let completeTimeout = null;
let keyboardAudioContext = null;
let startTime = null;

const keyboardSoundPresets = {
    soft: {
        label: 'Soft taps',
        type: 'triangle',
        volume: 0.12,
        tone: 230,
        endTone: 110,
        noise: 0.045,
        duration: 0.07
    },
    mechanical: {
        label: 'Mechanical clicks',
        type: 'square',
        volume: 0.16,
        tone: 320,
        endTone: 90,
        noise: 0.085,
        duration: 0.055
    },
    piano: {
        label: 'Piano notes',
        type: 'sine',
        volume: 0.13,
        tone: 440,
        endTone: 330,
        noise: 0.015,
        duration: 0.14
    },
    retro: {
        label: 'Retro blips',
        type: 'square',
        volume: 0.1,
        tone: 520,
        endTone: 260,
        noise: 0,
        duration: 0.09
    },
    off: {
        label: 'Off'
    }
};

const voiceStylePresets = {
    natural: { rate: 0.92, pitch: 1.0, volume: 1.0 },
    clear: { rate: 0.82, pitch: 1.02, volume: 1.0 },
    slow: { rate: 0.68, pitch: 1.0, volume: 1.0 },
    exam: { rate: 1.0, pitch: 0.98, volume: 1.0 }
};

// Statistics tracking
let currentSessionWPM = 0;
let currentSessionAccuracy = 100;

document.addEventListener('DOMContentLoaded', async () => {
    // Restore settings from LocalStorage
    keyboardLayoutSelect.value = localStorage.getItem('kg-keyboard-layout') || 'qwertz';
    levelSelect.value = localStorage.getItem('kg-level') || 'B2';
    categorySelect.value = localStorage.getItem('kg-category') || '';
    themeSelect.value = localStorage.getItem('kg-theme') || 'light';
    translationSelect.value = localStorage.getItem('kg-translation') || 'ar';
    voiceSelect.value = localStorage.getItem('kg-voice') || 'on';
    germanVoiceSelect.value = localStorage.getItem('kg-german-voice') || 'auto';
    voiceStyleSelect.value = localStorage.getItem('kg-voice-style') || 'natural';
    keyboardSoundSelect.value = localStorage.getItem('kg-keyboard-sound') || 'soft';

    // Apply theme
    applyTheme();
    
    // Load voices for speech synthesis
    if ('speechSynthesis' in window) {
        populateGermanVoices();
        if (window.speechSynthesis.onvoiceschanged !== undefined) {
            window.speechSynthesis.onvoiceschanged = populateGermanVoices;
        }
        setTimeout(populateGermanVoices, 250);
    }
    
    // Load categories from API first
    try {
        await loadCategories();
    } catch (error) {
        console.warn('Failed to load categories:', error);
    }
    
    // Load sentences from API
    try {
        await loadSentencesFromFastApi();
    } catch (error) {
        console.warn('Failed to load sentences:', error);
    }
    
    // Load random sentence from API
    try {
        await loadRandomSentenceFromFastApi();
    } catch (error) {
        console.warn('Failed to load random sentence, using fallback:', error);
        // Use fallback
        const fallback = sentenceBank[0] || fallbackSentences[0];
        setSentence(fallback, true);
    }
    
    // Initialize UI elements (after data is loaded)
    renderSentence();
    updateTranslation();
    updateTypingFeedback();

    // Attach event listeners
    typingInput.addEventListener('input', updateTypingFeedback);
    document.addEventListener('keydown', handleKeyDown);
    document.addEventListener('keyup', handleKeyUp);
    settingsToggle.addEventListener('click', toggleSettings);
    settingsClose.addEventListener('click', closeSettings);
    statsToggle.addEventListener('click', toggleStats);
    statsClose.addEventListener('click', closeStats);
    statsReset.addEventListener('click', resetStats);
    achievementsToggle.addEventListener('click', toggleAchievements);
    achievementsClose.addEventListener('click', closeAchievements);
    favoriteButton.addEventListener('click', toggleFavorite);
    keyboardLayoutSelect.addEventListener('change', handleKeyboardLayoutChange);
    levelSelect.addEventListener('change', handleLevelChange);
    categorySelect.addEventListener('change', handleCategoryChange);
    filterSelect.addEventListener('change', handleFilterChange);
    themeSelect.addEventListener('change', handleThemeChange);
    translationSelect.addEventListener('change', handleTranslationChange);
    voiceSelect.addEventListener('change', () => localStorage.setItem('kg-voice', voiceSelect.value));
    germanVoiceSelect.addEventListener('change', handleGermanVoiceChange);
    voiceStyleSelect.addEventListener('change', handleVoiceStyleChange);
    keyboardSoundSelect.addEventListener('change', handleKeyboardSoundChange);
    listenButton.addEventListener('click', () => speakGerman(currentSentence.german));
    quickListenButton.addEventListener('click', () => speakGerman(currentSentence.german));
    retryButton.addEventListener('click', retryCurrentSentence);
    skipButton.addEventListener('click', loadRandomSentenceFromFastApi);
    searchForm.addEventListener('submit', (event) => event.preventDefault());
    sentenceSearch.addEventListener('input', handleSearch);

    document.addEventListener('click', (event) => {
        if (!settingsPanel.contains(event.target) && !settingsToggle.contains(event.target)) {
            closeSettings();
        }
        if (!statsPanel.contains(event.target) && !statsToggle.contains(event.target)) {
            closeStats();
        }
        if (!achievementsPanel.contains(event.target) && !achievementsToggle.contains(event.target)) {
            closeAchievements();
        }
    });

    updateStatsDisplay();
    updateAchievementsDisplay();
    updateFavoriteButtonState();
});

async function loadSentencesFromFastApi() {
    try {
        const level = levelSelect.value || 'B2';
        const category = categorySelect.value;
        const params = new URLSearchParams({ level, limit: 100 });
        if (category) {
            params.append('category', category);
        }
        
        const response = await fetch(`${API_BASE_URL}/sentences?${params}`);
        if (!response.ok) {
            throw new Error(`API error: ${response.status} ${response.statusText}`);
        }

        let apiSentences = await response.json();
        
        if (!Array.isArray(apiSentences)) {
            throw new Error('API response is not an array');
        }
        
        // Filter by favorites if selected
        const filter = filterSelect.value;
        if (filter === 'favorites') {
            const favorites = getFavorites();
            apiSentences = apiSentences.filter(s => favorites.includes(s.id));
        }
        
        if (apiSentences.length > 0) {
            sentenceBank = apiSentences.map(normalizeApiSentence).filter(Boolean);
        }
        
        if (!sentenceBank.length) {
            console.warn('No sentences loaded, using fallback');
            sentenceBank = [...fallbackSentences];
        }
    } catch (error) {
        console.warn('Failed to load sentences from API:', error);
        sentenceBank = [...fallbackSentences];
    }
}

async function loadCategories() {
    try {
        const response = await fetch(`${API_BASE_URL}/categories`);
        if (!response.ok) {
            throw new Error(`API error: ${response.status} ${response.statusText}`);
        }

        const categories = await response.json();
        
        if (!Array.isArray(categories)) {
            throw new Error('Categories response is not an array');
        }
        
        // Clear existing options (except "All Categories")
        while (categorySelect.options.length > 1) {
            categorySelect.remove(1);
        }
        
        // Add categories
        categories.forEach((category) => {
            if (category) {  // Skip empty values
                const option = document.createElement('option');
                option.value = category;
                option.textContent = category;
                categorySelect.appendChild(option);
            }
        });
    } catch (error) {
        console.warn('Failed to load categories from API:', error);
        // Fallback: add default categories
        const defaultCategories = ['Daily Life', 'Food & Drinks', 'Education'];
        defaultCategories.forEach((category) => {
            const option = document.createElement('option');
            option.value = category;
            option.textContent = category;
            categorySelect.appendChild(option);
        });
    }
}

async function loadRandomSentenceFromFastApi() {
    try {
        const level = levelSelect.value || 'B2';
        const category = categorySelect.value;
        const params = new URLSearchParams({ level });
        if (category) {
            params.append('category', category);
        }
        
        const response = await fetch(`${API_BASE_URL}/sentences/random?${params}`);
        if (!response.ok) {
            throw new Error(`API error: ${response.status} ${response.statusText}`);
        }

        const sentence = await response.json();
        if (!sentence || !sentence.german_text) {
            throw new Error('Invalid sentence response from API');
        }
        
        const normalized = normalizeApiSentence(sentence);
        if (normalized) {
            setSentence(normalized, true);
            typingState.textContent = 'Ready';
        } else {
            throw new Error('Failed to normalize sentence');
        }
    } catch (error) {
        console.warn('Failed to load random sentence from API:', error);
        const fallback = sentenceBank[Math.floor(Math.random() * sentenceBank.length)] || fallbackSentences[0];
        if (fallback) {
            setSentence(fallback, true);
        }
        typingState.textContent = 'Offline';
    }
}

function normalizeApiSentence(sentence) {
    if (!sentence || typeof sentence !== 'object') {
        return null;
    }

    // Ensure all required fields exist
    if (!sentence.german_text || !sentence.english_translation || !sentence.arabic_translation) {
        console.warn('Incomplete sentence data:', sentence);
        return null;
    }

    return {
        id: sentence.id || Math.random(),
        german: sentence.german_text.trim(),
        en: sentence.english_translation.trim(),
        ar: sentence.arabic_translation.trim(),
        level: (sentence.level || 'B2').toUpperCase(),
        category: sentence.category || 'General'
    };
}

function renderSentence() {
    sentenceDisplay.innerHTML = '';

    if (!currentSentence || !currentSentence.german) {
        sentenceDisplay.textContent = 'No sentence loaded';
        return;
    }

    [...currentSentence.german].forEach((character, index) => {
        const span = document.createElement('span');
        span.textContent = character;
        span.dataset.index = index;
        sentenceDisplay.appendChild(span);
    });
}

function updateTranslation() {
    if (!currentSentence) {
        translationDisplay.textContent = 'No translation available';
        return;
    }

    const language = translationSelect.value || 'ar';
    const translation = currentSentence[language] || currentSentence.en || 'Translation not available';
    
    translationDisplay.textContent = translation;
    translationDisplay.lang = language === 'ar' ? 'ar' : 'en';
    translationDisplay.dir = language === 'ar' ? 'rtl' : 'ltr';
}

function updateTypingFeedback() {
    const typedText = typingInput.value;
    const targetText = currentSentence.german;
    const characters = [...sentenceDisplay.querySelectorAll('span')];
    let mistakes = 0;

    characters.forEach((span, index) => {
        span.className = '';

        if (index < typedText.length) {
            if (typedText[index] === targetText[index]) {
                span.classList.add('correct');
            } else {
                span.classList.add('wrong');
                mistakes += 1;
            }
        } else if (index === typedText.length) {
            span.classList.add('current');
        }
    });

    // Track start time for WPM calculation
    if (typedText.length > 0 && startTime === null) {
        startTime = Date.now();
    }

    // Calculate WPM
    let wpm = 0;
    if (startTime !== null && typedText.length > 0) {
        const timeElapsed = (Date.now() - startTime) / 1000 / 60; // Convert to minutes
        wpm = Math.round((typedText.length / 5) / timeElapsed);
    }

    const progress = Math.min(Math.round((typedText.length / targetText.length) * 100), 100) || 0;
    const accuracy = typedText.length
        ? Math.max(Math.round(((typedText.length - mistakes) / typedText.length) * 100), 0)
        : 100;

    progressBar.style.width = `${progress}%`;
    progressLabel.textContent = `${progress}%`;
    accuracyLabel.textContent = `${accuracy}%`;
    wpmLabel.textContent = `${wpm}`;
    typingInput.classList.toggle('has-error', mistakes > 0);
    updateNextKey(typedText.length);

    if (typedText === targetText && !isComplete) {
        isComplete = true;
        typingInput.classList.add('is-complete');
        typingState.textContent = '✓ Complete!';

        // Update statistics
        const finalWPM = wpm;
        const finalAccuracy = accuracy;
        const wordsTyped = typedText.split(/\s+/).length;
        updateStats(finalWPM, finalAccuracy, wordsTyped);
        
        // Check for perfect accuracy achievement
        if (finalAccuracy === 100) {
            unlockAchievement('perfect_accuracy');
        }
        
        currentSessionWPM = finalWPM;
        currentSessionAccuracy = finalAccuracy;

        if (voiceSelect.value === 'on') {
            speakGerman(targetText);
        }

        if (completeTimeout) clearTimeout(completeTimeout);
        completeTimeout = setTimeout(loadRandomSentenceFromFastApi, 1200);
    } else if (typedText !== targetText) {
        isComplete = false;
        typingInput.classList.remove('is-complete');
        
        if (mistakes > 0) {
            typingState.textContent = `⚠ ${mistakes} error${mistakes > 1 ? 's' : ''}`;
        } else {
            typingState.textContent = typedText.length ? '✓ Typing' : 'Ready';
        }
    }
}

function updateNextKey(index) {
    keyboardKeys.forEach((key) => key.classList.remove('next'));

    const nextCharacter = currentSentence.german[index];
    const normalized = normalizeKey(nextCharacter);
    const keyElements = findKey(normalized);

    // Show next character with emoji for clarity
    if (nextCharacter) {
        nextKeyLabel.textContent = printableKey(nextCharacter);
    } else {
        nextKeyLabel.textContent = '✓ Done';
    }

    if (keyElements && keyElements.length > 0) {
        keyElements.forEach((key) => {
            key.classList.add('next');
            // Add pulsing animation
            key.style.animation = 'nextPulse 1.2s ease-in-out infinite';
        });
    }
}

function printableKey(key) {
    const printMap = {
        ' ': '⎵ Space',
        'ä': 'ä',
        'ö': 'ö',
        'ü': 'ü',
        'ß': 'ß',
        '.': '·',
        ',': '‚',
        '!': '!',
        '?': '?'
    };
    
    return printMap[key] || key.toUpperCase();
}

function handleKeyDown(event) {
    const normalized = normalizeKey(event.key);
    setKeyActive(normalized, true);

    if (!event.repeat && shouldPlayKeyboardSound(event)) {
        playKeyboardClick(event.key);
    }

    if (event.key === 'Escape') {
        closeSettings();
    }
}

function handleKeyUp(event) {
    const normalized = normalizeKey(event.key);
    setKeyActive(normalized, false);
}

function setKeyActive(normalized, isActive) {
    const keys = keyboardKeys.filter((key) => key.dataset.key === normalized);
    keys.forEach((key) => key.classList.toggle('active', isActive));
}

function shouldPlayKeyboardSound(event) {
    const editableTargets = ['TEXTAREA', 'INPUT'];
    return editableTargets.includes(event.target.tagName) && event.target.id === 'typing-input';
}

function playKeyboardClick(key) {
    const presetName = keyboardSoundSelect.value || 'soft';
    const preset = keyboardSoundPresets[presetName] || keyboardSoundPresets.soft;

    if (presetName === 'off') {
        return;
    }

    if (!window.AudioContext && !window.webkitAudioContext) {
        return;
    }

    const AudioContextConstructor = window.AudioContext || window.webkitAudioContext;
    keyboardAudioContext = keyboardAudioContext || new AudioContextConstructor();
    if (keyboardAudioContext.state === 'suspended') {
        keyboardAudioContext.resume();
    }

    const now = keyboardAudioContext.currentTime;
    const isSpace = key === ' ';
    const isDelete = key === 'Backspace' || key === 'Delete';
    const isEnter = key === 'Enter';
    const isLetter = /^[a-zA-ZäöüÄÖÜßẞ]$/.test(key);
    const keyOffset = isLetter ? key.toLowerCase().charCodeAt(0) % 7 : 0;
    const startFrequency = (isSpace ? preset.tone * 0.72 : isDelete ? preset.tone * 0.58 : isEnter ? preset.tone * 0.66 : preset.tone) + keyOffset * 18;
    const endFrequency = isSpace ? preset.endTone * 0.82 : isDelete ? preset.endTone * 0.7 : isEnter ? preset.endTone * 0.75 : preset.endTone;

    // Create white noise for more realistic keyboard sound
    const bufferSize = Math.max(1, Math.floor(keyboardAudioContext.sampleRate * preset.duration));
    const noiseBuffer = keyboardAudioContext.createBuffer(1, bufferSize, keyboardAudioContext.sampleRate);
    const noiseData = noiseBuffer.getChannelData(0);
    for (let i = 0; i < bufferSize; i++) {
        noiseData[i] = Math.random() * 2 - 1;
    }

    const noiseSource = keyboardAudioContext.createBufferSource();
    noiseSource.buffer = noiseBuffer;

    // Create tone oscillator
    const oscillator = keyboardAudioContext.createOscillator();
    
    // Create gains for tone and noise
    const toneGain = keyboardAudioContext.createGain();
    const noiseGain = keyboardAudioContext.createGain();
    const masterGain = keyboardAudioContext.createGain();

    // Configure oscillator (tone)
    oscillator.type = preset.type;
    oscillator.frequency.setValueAtTime(startFrequency, now);
    oscillator.frequency.exponentialRampToValueAtTime(Math.max(1, endFrequency), now + preset.duration * 0.62);

    // Configure tone gain
    toneGain.gain.setValueAtTime(0, now);
    toneGain.gain.exponentialRampToValueAtTime(isSpace ? preset.volume * 0.7 : preset.volume, now + 0.008);
    toneGain.gain.exponentialRampToValueAtTime(0.001, now + preset.duration);

    // Configure noise gain
    noiseGain.gain.setValueAtTime(0, now);
    if (preset.noise > 0) {
        noiseGain.gain.exponentialRampToValueAtTime(isSpace ? preset.noise * 0.8 : preset.noise, now + 0.006);
    }
    noiseGain.gain.exponentialRampToValueAtTime(0.001, now + preset.duration);

    // Configure master gain
    masterGain.gain.setValueAtTime(0.18, now);

    // Connect all nodes
    oscillator.connect(toneGain);
    noiseSource.connect(noiseGain);
    toneGain.connect(masterGain);
    noiseGain.connect(masterGain);
    masterGain.connect(keyboardAudioContext.destination);

    // Start and stop
    oscillator.start(now);
    oscillator.stop(now + preset.duration);
    noiseSource.start(now);
    noiseSource.stop(now + preset.duration);
}

function normalizeKey(key) {
    if (!key) {
        return '';
    }

    const aliases = {
        Backspace: 'backspace',
        Tab: 'tab',
        CapsLock: 'capslock',
        Enter: 'enter',
        Shift: 'shift',
        ' ': ' ',
        'Ä': 'ä',
        'Ö': 'ö',
        'Ü': 'ü',
        'ß': 'ß',
        'ẞ': 'ß'
    };

    return aliases[key] || key.toLowerCase();
}

function findKey(normalizedKey) {
    return keyboardKeys.filter((key) => key.dataset.key === normalizedKey);
}

function toggleSettings() {
    const willOpen = !settingsPanel.classList.contains('is-open');
    settingsPanel.classList.toggle('is-open', willOpen);
    settingsToggle.classList.toggle('is-open', willOpen);
    settingsToggle.setAttribute('aria-expanded', String(willOpen));
}

function closeSettings() {
    settingsPanel.classList.remove('is-open');
    settingsToggle.classList.remove('is-open');
    settingsToggle.setAttribute('aria-expanded', 'false');
}

function handleThemeChange() {
    localStorage.setItem('kg-theme', themeSelect.value);
    applyTheme();
}

function applyTheme() {
    document.body.dataset.theme = themeSelect.value;
}

function handleTranslationChange() {
    localStorage.setItem('kg-translation', translationSelect.value);
    updateTranslation();
}

function handleLevelChange() {
    localStorage.setItem('kg-level', levelSelect.value);
    levelDisplay.textContent = `${levelSelect.value} German`;
    loadSentencesFromFastApi();
    loadRandomSentenceFromFastApi();
}

function handleCategoryChange() {
    localStorage.setItem('kg-category', categorySelect.value);
    loadSentencesFromFastApi();
    loadRandomSentenceFromFastApi();
}

function handleKeyboardLayoutChange() {
    localStorage.setItem('kg-keyboard-layout', keyboardLayoutSelect.value);
    const layout = keyboardLayoutSelect.value;
    const layoutName = keyboardLayouts[layout]?.name || 'QWERTZ';
    const keyboardHeader = document.querySelector('.keyboard-header h2');
    if (keyboardHeader) {
        keyboardHeader.textContent = `${layoutName} Keyboard`;
    }
}

function populateGermanVoices() {
    if (!('speechSynthesis' in window)) {
        germanVoiceSelect.innerHTML = '<option value="auto">Speech not supported</option>';
        germanVoiceSelect.disabled = true;
        return;
    }

    const selectedVoice = localStorage.getItem('kg-german-voice') || germanVoiceSelect.value || 'auto';
    const voices = window.speechSynthesis
        .getVoices()
        .filter((voice) => voice.lang && voice.lang.toLowerCase().startsWith('de'))
        .sort((a, b) => scoreGermanVoice(b) - scoreGermanVoice(a) || a.name.localeCompare(b.name));

    germanVoiceSelect.innerHTML = '';

    const autoOption = document.createElement('option');
    autoOption.value = 'auto';
    autoOption.textContent = voices.length ? `Auto: ${voices[0].name}` : 'Auto German voice';
    germanVoiceSelect.appendChild(autoOption);

    voices.forEach((voice) => {
        const option = document.createElement('option');
        option.value = voice.voiceURI;
        option.textContent = `${voice.name} (${voice.lang})`;
        germanVoiceSelect.appendChild(option);
    });

    germanVoiceSelect.disabled = voices.length === 0;
    germanVoiceSelect.value = [...germanVoiceSelect.options].some((option) => option.value === selectedVoice)
        ? selectedVoice
        : 'auto';
}

function scoreGermanVoice(voice) {
    const name = `${voice.name} ${voice.voiceURI}`.toLowerCase();
    let score = 0;

    if (voice.lang && voice.lang.toLowerCase() === 'de-de') score += 30;
    if (voice.default) score += 8;
    if (name.includes('natural') || name.includes('neural') || name.includes('premium')) score += 18;
    if (name.includes('google') || name.includes('microsoft') || name.includes('apple')) score += 10;
    if (name.includes('katja') || name.includes('anna') || name.includes('markus') || name.includes('conrad')) score += 6;
    if (!voice.localService) score += 3;

    return score;
}

function getPreferredGermanVoice() {
    if (!('speechSynthesis' in window)) {
        return null;
    }

    const voices = window.speechSynthesis.getVoices();
    const selectedVoice = germanVoiceSelect.value || 'auto';

    if (selectedVoice !== 'auto') {
        const exactVoice = voices.find((voice) => voice.voiceURI === selectedVoice);
        if (exactVoice) {
            return exactVoice;
        }
    }

    return voices
        .filter((voice) => voice.lang && voice.lang.toLowerCase().startsWith('de'))
        .sort((a, b) => scoreGermanVoice(b) - scoreGermanVoice(a))[0] || null;
}

function handleGermanVoiceChange() {
    localStorage.setItem('kg-german-voice', germanVoiceSelect.value);
    speakGerman('Guten Tag. Ich lese Deutsch natürlich und deutlich.');
}

function handleVoiceStyleChange() {
    localStorage.setItem('kg-voice-style', voiceStyleSelect.value);
    speakGerman('So klingt dieser Lesestil auf Deutsch.');
}

function handleKeyboardSoundChange() {
    localStorage.setItem('kg-keyboard-sound', keyboardSoundSelect.value);
    if (keyboardSoundSelect.value !== 'off') {
        playKeyboardClick('Enter');
    }
}

function toggleStats() {
    const willOpen = !statsPanel.classList.contains('is-open');
    statsPanel.classList.toggle('is-open', willOpen);
    statsToggle.classList.toggle('is-open', willOpen);
    statsToggle.setAttribute('aria-expanded', String(willOpen));
}

function closeStats() {
    statsPanel.classList.remove('is-open');
    statsToggle.classList.remove('is-open');
    statsToggle.setAttribute('aria-expanded', 'false');
}

function getStats() {
    const statsStr = localStorage.getItem('kg-stats');
    return statsStr ? JSON.parse(statsStr) : {
        sessions: 0,
        totalAccuracy: 0,
        totalWPM: 0,
        totalWords: 0,
        bestWPM: 0,
        bestAccuracy: 0
    };
}

function saveStats(stats) {
    localStorage.setItem('kg-stats', JSON.stringify(stats));
}

function updateStats(finalWPM, finalAccuracy, wordsTyped) {
    const stats = getStats();
    stats.sessions += 1;
    stats.totalAccuracy += finalAccuracy;
    stats.totalWPM += finalWPM;
    stats.totalWords += wordsTyped;
    stats.bestWPM = Math.max(stats.bestWPM, finalWPM);
    stats.bestAccuracy = Math.max(stats.bestAccuracy, finalAccuracy);
    saveStats(stats);
    updateStatsDisplay();
    checkAchievements(stats);
}

function updateStatsDisplay() {
    const stats = getStats();
    const avgAccuracy = stats.sessions > 0 ? Math.round(stats.totalAccuracy / stats.sessions) : 0;
    const avgWPM = stats.sessions > 0 ? Math.round(stats.totalWPM / stats.sessions) : 0;
    
    document.getElementById('stat-sessions').textContent = stats.sessions;
    document.getElementById('stat-avg-accuracy').textContent = `${avgAccuracy}%`;
    document.getElementById('stat-avg-wpm').textContent = avgWPM;
    document.getElementById('stat-total-words').textContent = stats.totalWords;
    document.getElementById('stat-best-wpm').textContent = stats.bestWPM;
    document.getElementById('stat-best-accuracy').textContent = `${stats.bestAccuracy}%`;
}

function resetStats() {
    if (confirm('Are you sure you want to reset all statistics?')) {
        saveStats({
            sessions: 0,
            totalAccuracy: 0,
            totalWPM: 0,
            totalWords: 0,
            bestWPM: 0,
            bestAccuracy: 0
        });
        updateStatsDisplay();
    }
}

function getFavorites() {
    const favStr = localStorage.getItem('kg-favorites');
    return favStr ? JSON.parse(favStr) : [];
}

function saveFavorites(favorites) {
    localStorage.setItem('kg-favorites', JSON.stringify(favorites));
}

function isFavorite(sentenceId) {
    return getFavorites().includes(sentenceId);
}

function toggleFavorite() {
    if (!currentSentence.id) {
        return;
    }

    const favorites = getFavorites();
    const index = favorites.indexOf(currentSentence.id);
    
    if (index > -1) {
        favorites.splice(index, 1);
    } else {
        favorites.push(currentSentence.id);
    }
    
    saveFavorites(favorites);
    updateFavoriteButtonState();
}

function updateFavoriteButtonState() {
    if (!currentSentence.id) {
        favoriteButton.textContent = '♡';
        favoriteButton.classList.remove('active');
        return;
    }

    if (isFavorite(currentSentence.id)) {
        favoriteButton.textContent = '♥';
        favoriteButton.classList.add('active');
    } else {
        favoriteButton.textContent = '♡';
        favoriteButton.classList.remove('active');
    }
}

function handleFilterChange() {
    localStorage.setItem('kg-filter', filterSelect.value);
    loadSentencesFromFastApi();
    loadRandomSentenceFromFastApi();
}

function retryCurrentSentence() {
    if (completeTimeout) {
        clearTimeout(completeTimeout);
        completeTimeout = null;
    }

    typingInput.value = '';
    typingInput.focus();
    typingInput.classList.remove('has-error', 'is-complete');
    isComplete = false;
    startTime = null;
    typingState.textContent = 'Ready';
    updateTypingFeedback();
}

function toggleAchievements() {
    const willOpen = !achievementsPanel.classList.contains('is-open');
    achievementsPanel.classList.toggle('is-open', willOpen);
    achievementsToggle.classList.toggle('is-open', willOpen);
    achievementsToggle.setAttribute('aria-expanded', String(willOpen));
}

function closeAchievements() {
    achievementsPanel.classList.remove('is-open');
    achievementsToggle.classList.remove('is-open');
    achievementsToggle.setAttribute('aria-expanded', 'false');
}

function getUnlockedAchievements() {
    const unlockedStr = localStorage.getItem('kg-achievements');
    return unlockedStr ? JSON.parse(unlockedStr) : [];
}

function unlockAchievement(achievementId) {
    const unlocked = getUnlockedAchievements();
    if (!unlocked.includes(achievementId)) {
        unlocked.push(achievementId);
        localStorage.setItem('kg-achievements', JSON.stringify(unlocked));
        updateAchievementsDisplay();
    }
}

function checkAchievements(stats) {
    const unlocked = getUnlockedAchievements();

    // First session achievement
    if (stats.sessions === 1) {
        unlockAchievement('first_session');
    }

    // Dedicated (10 sessions)
    if (stats.sessions >= 10) {
        unlockAchievement('ten_sessions');
    }

    // Master (50 sessions)
    if (stats.sessions >= 50) {
        unlockAchievement('fifty_sessions');
    }

    // Speed demon (60 WPM)
    if (stats.bestWPM >= 60) {
        unlockAchievement('speed_demon');
    }

    // Prolific (500 words)
    if (stats.totalWords >= 500) {
        unlockAchievement('five_hundred_words');
    }

    // Collector (10 favorites)
    if (getFavorites().length >= 10) {
        unlockAchievement('ten_favorites');
    }
}

function updateAchievementsDisplay() {
    const unlocked = getUnlockedAchievements();
    achievementsList.innerHTML = '';

    achievements.forEach((achievement) => {
        const div = document.createElement('div');
        div.className = 'achievement-item ' + (unlocked.includes(achievement.id) ? 'unlocked' : 'locked');
        div.innerHTML = `
            <div class="achievement-icon">${achievement.icon}</div>
            <div class="achievement-info">
                <strong>${achievement.name}</strong>
                <p>${achievement.description}</p>
            </div>
        `;
        achievementsList.appendChild(div);
    });
}

function handleSearch() {
    const query = sentenceSearch.value.trim().toLowerCase();

    if (!query) {
        loadRandomSentenceFromFastApi();
        return;
    }

    const match = sentenceBank.find((sentence) => {
        return sentence.german.toLowerCase().includes(query)
            || sentence.en.toLowerCase().includes(query)
            || sentence.ar.includes(query);
    });

    if (match) {
        setSentence(match);
    }
}

function setSentence(sentence, force = false) {
    if (!sentence || (!force && sentence.german === currentSentence.german)) {
        return;
    }

    currentSentence = sentence;
    typingInput.value = '';
    typingInput.classList.remove('has-error', 'is-complete');
    isComplete = false;
    startTime = null;
    renderSentence();
    updateTranslation();
    updateTypingFeedback();
    updateFavoriteButtonState();
}

function speakGerman(text) {
    if (!('speechSynthesis' in window)) {
        console.warn('Speech synthesis not supported');
        return;
    }

    window.speechSynthesis.cancel();

    const utterance = new SpeechSynthesisUtterance(text);
    const style = voiceStylePresets[voiceStyleSelect.value] || voiceStylePresets.natural;
    const germanVoice = getPreferredGermanVoice();

    utterance.lang = 'de-DE';
    utterance.rate = style.rate;
    utterance.pitch = style.pitch;
    utterance.volume = style.volume;

    if (germanVoice) {
        utterance.voice = germanVoice;
        utterance.lang = germanVoice.lang || 'de-DE';
    }

    try {
        window.speechSynthesis.speak(utterance);
    } catch (error) {
        console.warn('Speech synthesis error:', error);
    }
}
