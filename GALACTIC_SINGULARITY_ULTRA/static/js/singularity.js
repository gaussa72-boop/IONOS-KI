/**
 * GALACTIC SINGULARITY ULTRA - JavaScript
 * ========================================
 * Interaktive Singularität mit KI-Chat-Portal
 */

// =====================================================
// GLOBAL VARIABLES
// =====================================================

let isPortalOpen = false;
let currentModule = 'all';
const canvas = document.getElementById('singularity-canvas');
const ctx = canvas ? canvas.getContext('2d') : null;
let animationFrame;
let particles = [];

// =====================================================
// SINGULARITY ANIMATION
// =====================================================

function initCanvas() {
    if (!canvas) return;

    canvas.width = 300;
    canvas.height = 300;

    // Partikel erstellen
    for (let i = 0; i < 150; i++) {
        particles.push({
            angle: Math.random() * Math.PI * 2,
            radius: Math.random() * 120 + 30,
            speed: Math.random() * 0.02 + 0.005,
            size: Math.random() * 2 + 0.5,
            color: `hsl(${Math.random() * 60 + 30}, 100%, ${Math.random() * 30 + 50}%)`
        });
    }

    animateSingularity();
}

function animateSingularity() {
    if (!ctx) return;

    ctx.fillStyle = 'rgba(10, 10, 15, 0.1)';
    ctx.fillRect(0, 0, canvas.width, canvas.height);

    const centerX = canvas.width / 2;
    const centerY = canvas.height / 2;

    // Zeichne spiralförmige Partikel
    particles.forEach(particle => {
        particle.angle += particle.speed;
        particle.radius -= 0.1;

        // Reset wenn zu nah am Zentrum
        if (particle.radius < 10) {
            particle.radius = 140;
            particle.angle = Math.random() * Math.PI * 2;
        }

        const x = centerX + Math.cos(particle.angle) * particle.radius;
        const y = centerY + Math.sin(particle.angle) * particle.radius;

        ctx.beginPath();
        ctx.arc(x, y, particle.size, 0, Math.PI * 2);
        ctx.fillStyle = particle.color;
        ctx.fill();

        // Leuchteffekt
        ctx.shadowBlur = 10;
        ctx.shadowColor = particle.color;
    });

    // Zentrum-Glow
    const gradient = ctx.createRadialGradient(centerX, centerY, 0, centerX, centerY, 50);
    gradient.addColorStop(0, 'rgba(255, 215, 0, 0.8)');
    gradient.addColorStop(0.5, 'rgba(155, 89, 182, 0.4)');
    gradient.addColorStop(1, 'transparent');

    ctx.beginPath();
    ctx.arc(centerX, centerY, 50, 0, Math.PI * 2);
    ctx.fillStyle = gradient;
    ctx.fill();

    animationFrame = requestAnimationFrame(animateSingularity);
}

// =====================================================
// PORTAL FUNCTIONS
// =====================================================

function openPortal() {
    if (isPortalOpen) return;

    isPortalOpen = true;

    // Sound abspielen (falls verfügbar)
    const sound = document.getElementById('portal-sound');
    if (sound) {
        sound.currentTime = 0;
        sound.play().catch(() => {}); // Ignoriere Autoplay-Fehler
    }

    // Singularität verstecken
    const singularityContainer = document.getElementById('singularity-container');
    singularityContainer.classList.remove('active');
    singularityContainer.classList.add('hidden');

    // Chat-Portal zeigen
    setTimeout(() => {
        const chatPortal = document.getElementById('chat-portal');
        chatPortal.classList.remove('hidden');
        chatPortal.classList.add('active');

        // Fokus auf Input
        document.getElementById('chat-input').focus();
    }, 300);

    // Animation stoppen
    if (animationFrame) {
        cancelAnimationFrame(animationFrame);
    }
}

function minimizePortal() {
    isPortalOpen = false;

    // Chat-Portal verstecken
    const chatPortal = document.getElementById('chat-portal');
    chatPortal.classList.remove('active');
    chatPortal.classList.add('hidden');

    // Singularität zeigen
    setTimeout(() => {
        const singularityContainer = document.getElementById('singularity-container');
        singularityContainer.classList.remove('hidden');
        singularityContainer.classList.add('active');

        // Animation neu starten
        animateSingularity();
    }, 300);
}

// =====================================================
// CHAT FUNCTIONS
// =====================================================

async function sendMessage() {
    const input = document.getElementById('chat-input');
    const message = input.value.trim();

    if (!message) return;

    // User-Nachricht anzeigen
    addMessage(message, 'user');
    input.value = '';

    // Typing-Indikator zeigen
    showTypingIndicator();

    try {
        // Modul-Präfix hinzufügen wenn spezifisches Modul ausgewählt
        let finalMessage = message;
        if (currentModule !== 'all') {
            finalMessage = `${currentModule} ${message}`;
        }

        const response = await fetch('/chat', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ message: finalMessage })
        });

        const data = await response.json();

        hideTypingIndicator();

        if (data.error) {
            addMessage(`⚠️ Fehler: ${data.error}`, 'ai');
        } else {
            addMessage(data.response, 'ai');
        }

    } catch (error) {
        hideTypingIndicator();
        addMessage('⚠️ Verbindungsfehler zur Singularität. Versuche es erneut.', 'ai');
        console.error('Chat error:', error);
    }
}

function quickSend(message) {
    document.getElementById('chat-input').value = message;
    sendMessage();
}

function addMessage(content, type) {
    const messagesContainer = document.getElementById('chat-messages');

    const messageDiv = document.createElement('div');
    messageDiv.className = `message ${type === 'user' ? 'user-message' : 'ai-message'}`;

    const avatar = type === 'user' ? '👤' : '🌌';
    const name = type === 'user' ? 'Du' : 'Galaktische Singularität';

    // Formatiere den Content (unterstützt Zeilenumbrüche)
    const formattedContent = content.split('\n').map(line => `<p>${escapeHtml(line)}</p>`).join('');

    messageDiv.innerHTML = `
        <div class="message-avatar">${avatar}</div>
        <div class="message-content">
            <strong>${name}</strong>
            ${formattedContent}
        </div>
    `;

    messagesContainer.appendChild(messageDiv);

    // Scroll zum Ende
    messagesContainer.scrollTop = messagesContainer.scrollHeight;
}

function escapeHtml(text) {
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
}

function showTypingIndicator() {
    document.getElementById('typing-indicator').classList.remove('hidden');
}

function hideTypingIndicator() {
    document.getElementById('typing-indicator').classList.add('hidden');
}

// =====================================================
// MODULE SELECTION
// =====================================================

function initModuleButtons() {
    const moduleButtons = document.querySelectorAll('.module-btn');

    moduleButtons.forEach(btn => {
        btn.addEventListener('click', () => {
            // Aktiven Button aktualisieren
            moduleButtons.forEach(b => b.classList.remove('active'));
            btn.classList.add('active');

            // Modul setzen
            currentModule = btn.dataset.module;

            // Feedback
            const moduleNames = {
                'all': 'Alle Module',
                'quantum': 'Quantum AI',
                'blume': 'Lebensblume AI',
                'spirit': 'Urspirit AI'
            };

            // Optional: Kurze Bestätigung im Chat
            // addMessage(`${moduleNames[currentModule]} aktiviert ✓`, 'ai');
        });
    });
}

// =====================================================
// KEYBOARD SHORTCUTS
// =====================================================

function initKeyboardShortcuts() {
    document.addEventListener('keydown', (e) => {
        // Enter zum Senden
        if (e.key === 'Enter' && !e.shiftKey) {
            const input = document.getElementById('chat-input');
            if (document.activeElement === input) {
                e.preventDefault();
                sendMessage();
            }
        }

        // Escape zum Minimieren
        if (e.key === 'Escape' && isPortalOpen) {
            minimizePortal();
        }

        // Space zum Öffnen (wenn nicht im Input)
        if (e.key === ' ' && !isPortalOpen && document.activeElement.tagName !== 'INPUT') {
            e.preventDefault();
            openPortal();
        }
    });
}

// =====================================================
// VISUAL EFFECTS
// =====================================================

function addParticleEffect(x, y) {
    // Erstelle temporäre Partikel beim Klicken
    for (let i = 0; i < 10; i++) {
        const particle = document.createElement('div');
        particle.style.cssText = `
            position: fixed;
            left: ${x}px;
            top: ${y}px;
            width: 5px;
            height: 5px;
            background: gold;
            border-radius: 50%;
            pointer-events: none;
            z-index: 9999;
            animation: particleFade 1s ease-out forwards;
        `;

        const angle = (Math.PI * 2 / 10) * i;
        const distance = 50 + Math.random() * 50;
        const tx = Math.cos(angle) * distance;
        const ty = Math.sin(angle) * distance;

        particle.style.setProperty('--tx', `${tx}px`);
        particle.style.setProperty('--ty', `${ty}px`);

        document.body.appendChild(particle);

        setTimeout(() => particle.remove(), 1000);
    }
}

// CSS für Partikel-Animation hinzufügen
const style = document.createElement('style');
style.textContent = `
    @keyframes particleFade {
        0% {
            transform: translate(0, 0) scale(1);
            opacity: 1;
        }
        100% {
            transform: translate(var(--tx), var(--ty)) scale(0);
            opacity: 0;
        }
    }
`;
document.head.appendChild(style);

// =====================================================
// INITIALIZATION
// =====================================================

document.addEventListener('DOMContentLoaded', () => {
    console.log('🌌 Galaktische Singularität wird initialisiert...');

    initCanvas();
    initModuleButtons();
    initKeyboardShortcuts();

    // Klick-Effekt auf Singularität
    const singularity = document.getElementById('singularity');
    if (singularity) {
        singularity.addEventListener('click', (e) => {
            addParticleEffect(e.clientX, e.clientY);
        });
    }

    console.log('✨ Singularität bereit!');
});

// =====================================================
// EASTER EGGS
// =====================================================

// Konami-Code Easter Egg
let konamiCode = [];
const konamiSequence = [38, 38, 40, 40, 37, 39, 37, 39, 66, 65];

document.addEventListener('keydown', (e) => {
    konamiCode.push(e.keyCode);
    konamiCode = konamiCode.slice(-10);

    if (konamiCode.join(',') === konamiSequence.join(',')) {
        document.body.style.animation = 'rainbow 2s linear infinite';
        setTimeout(() => {
            document.body.style.animation = '';
        }, 5000);

        if (isPortalOpen) {
            addMessage('🎮 KONAMI CODE AKTIVIERT! Du hast das geheime Wissen freigeschaltet! 🌈✨', 'ai');
        }
    }
});

// Rainbow Animation CSS
const rainbowStyle = document.createElement('style');
rainbowStyle.textContent = `
    @keyframes rainbow {
        0% { filter: hue-rotate(0deg); }
        100% { filter: hue-rotate(360deg); }
    }
`;
document.head.appendChild(rainbowStyle);
