import SwiftUI

// MARK: - App Entry Point
@main
struct QuantumKIApp: App {
    var body: some Scene {
        WindowGroup {
            ContentView()
                .preferredColorScheme(.dark)
        }
    }
}

// MARK: - Main Content View (Sacred Geometry + Agents)
struct ContentView: View {
    @State private var activeAgent: KIAgent = .ionos7
    @State private var showChat = false
    @State private var chatMessages: [ChatMessage] = []
    @State private var inputText = ""

    var body: some View {
        ZStack {
            // Hintergrund
            RadialGradient(
                gradient: Gradient(colors: [Color(red: 0.04, green: 0.04, blue: 0.1), .black]),
                center: .center,
                startRadius: 0,
                endRadius: 500
            )
            .ignoresSafeArea()

            VStack {
                // MARK: - Info Panel (Oben)
                HStack {
                    VStack(alignment: .leading, spacing: 4) {
                        Text("Quantum Meta Core")
                            .font(.headline)
                            .foregroundColor(.gold)
                        Text("KI-Agenten Zentrale")
                            .font(.caption)
                            .foregroundColor(.cyan)
                        Text("10 Agenten online")
                            .font(.caption2)
                            .foregroundColor(.green)
                    }
                    Spacer()
                }
                .padding(12)
                .background(Color.gold.opacity(0.1))
                .border(Color.gold, width: 2)
                .cornerRadius(10)
                .padding()

                Spacer()

                // MARK: - Sacred Geometry Canvas
                SacredGeometryView()
                    .frame(height: 500)

                Spacer()

                // MARK: - KI-Agenten Grid (Spiegel-Buttons)
                VStack(spacing: 16) {
                    Text("KI-Rubriken")
                        .font(.title2)
                        .foregroundColor(.gold)

                    VStack(spacing: 12) {
                        HStack(spacing: 12) {
                            AgentButtonView(agent: .singulos, isActive: activeAgent == .singulos) {
                                activeAgent = .singulos
                                showChat = true
                            }
                            AgentButtonView(agent: .ionos7, isActive: activeAgent == .ionos7) {
                                activeAgent = .ionos7
                                showChat = true
                            }
                            AgentButtonView(agent: .ultra, isActive: activeAgent == .ultra) {
                                activeAgent = .ultra
                                showChat = true
                            }
                        }

                        HStack(spacing: 12) {
                            AgentButtonView(agent: .nexus, isActive: activeAgent == .nexus) {
                                activeAgent = .nexus
                                showChat = true
                            }
                            AgentButtonView(agent: .quantum, isActive: activeAgent == .quantum) {
                                activeAgent = .quantum
                                showChat = true
                            }
                            AgentButtonView(agent: .spark, isActive: activeAgent == .spark) {
                                activeAgent = .spark
                                showChat = true
                            }
                        }

                        HStack(spacing: 12) {
                            AgentButtonView(agent: .nova, isActive: activeAgent == .nova) {
                                activeAgent = .nova
                                showChat = true
                            }
                            AgentButtonView(agent: .zenith, isActive: activeAgent == .zenith) {
                                activeAgent = .zenith
                                showChat = true
                            }
                            AgentButtonView(agent: .aether, isActive: activeAgent == .aether) {
                                activeAgent = .aether
                                showChat = true
                            }
                        }

                        HStack(spacing: 12) {
                            AgentButtonView(agent: .infinity, isActive: activeAgent == .infinity) {
                                activeAgent = .infinity
                                showChat = true
                            }
                            Spacer()
                            Spacer()
                        }
                    }
                    .padding(12)
                    .background(Color.black.opacity(0.3))
                    .cornerRadius(15)
                }
                .padding()

                Spacer()
            }

            // MARK: - Chat Sheet (Oben)
            if showChat {
                ChatSheetView(
                    agent: $activeAgent,
                    messages: $chatMessages,
                    inputText: $inputText,
                    isPresented: $showChat
                )
            }
        }
    }
}

// MARK: - Agent Model
enum KIAgent: String, CaseIterable {
    case singulos = "Singulos"
    case ionos7 = "IONOS-7"
    case ultra = "Ultra"
    case nexus = "Nexus"
    case quantum = "Quantum"
    case spark = "Spark"
    case nova = "Nova"
    case zenith = "Zenith"
    case aether = "Aether"
    case infinity = "Infinity"

    var emoji: String {
        switch self {
        case .singulos: return "🌟"
        case .ionos7: return "⚡"
        case .ultra: return "🚀"
        case .nexus: return "🧠"
        case .quantum: return "⚛️"
        case .spark: return "✨"
        case .nova: return "💫"
        case .zenith: return "🔱"
        case .aether: return "🌌"
        case .infinity: return "∞"
        }
    }

    var color: Color {
        switch self {
        case .singulos, .zenith: return .gold
        case .ionos7, .nova: return .cyan
        case .ultra: return Color(red: 1.0, green: 0.08, blue: 0.58)
        case .nexus, .aether: return Color(red: 0.58, green: 0.44, blue: 0.86)
        case .quantum, .infinity: return .green
        case .spark: return Color(red: 1.0, green: 0.40, blue: 0.28)
        }
    }

    var description: String {
        switch self {
        case .singulos: return "Singularität der Intelligenz"
        case .ionos7: return "IONOS Cloud KI"
        case .ultra: return "Ultra Performance"
        case .nexus: return "Nexus Verbindungen"
        case .quantum: return "Quantencomputing"
        case .spark: return "Kreative Funktionen"
        case .nova: return "Supernova Energie"
        case .zenith: return "Höchste Leistung"
        case .aether: return "Ätherische Intelligenz"
        case .infinity: return "Unendliche Möglichkeiten"
        }
    }
}

// MARK: - Chat Message Model
struct ChatMessage: Identifiable {
    let id = UUID()
    let agent: KIAgent
    let content: String
    let isUser: Bool
    let timestamp: Date = Date()
}

// MARK: - Agent Button
struct AgentButtonView: View {
    let agent: KIAgent
    let isActive: Bool
    let action: () -> Void

    var body: some View {
        Button(action: action) {
            VStack(spacing: 4) {
                Text(agent.emoji)
                    .font(.system(size: 28))
                Text(agent.rawValue)
                    .font(.caption)
                    .foregroundColor(.white)
                    .lineLimit(1)
            }
            .frame(maxWidth: .infinity)
            .frame(height: 100)
            .background(
                isActive ?
                RadialGradient(
                    gradient: Gradient(colors: [Color.green, agent.color]),
                    center: .center,
                    startRadius: 0,
                    endRadius: 50
                ) :
                RadialGradient(
                    gradient: Gradient(colors: [agent.color, Color.black]),
                    center: .center,
                    startRadius: 0,
                    endRadius: 50
                )
            )
            .border(isActive ? Color.green : agent.color, width: 2)
            .cornerRadius(50)
            .shadow(color: isActive ? Color.green : agent.color, radius: 10)
        }
    }
}

// MARK: - Sacred Geometry Canvas
struct SacredGeometryView: View {
    var body: some View {
        Canvas { context in
            let rect = CGRect(x: 0, y: 0, width: 300, height: 300)
            let centerX = rect.midX
            let centerY = rect.midY

            // Zentral-Kreis
            let centralPath = Path(ellipseIn: CGRect(x: centerX - 15, y: centerY - 15, width: 30, height: 30))
            var centralStroke = StrokeStyle()
            centralStroke.lineWidth = 2
            context.stroke(centralPath, with: .color(.gold), style: centralStroke)

            // Blütenblätter (6er-Muster)
            for i in 0..<6 {
                let angle = CGFloat(i) / 6 * CGFloat.pi * 2
                let x = centerX + cos(angle) * 80
                let y = centerY + sin(angle) * 80
                let petalPath = Path(ellipseIn: CGRect(x: x - 30, y: y - 30, width: 60, height: 60))
                context.stroke(petalPath, with: .color(.gold.opacity(0.6)), style: centralStroke)
            }

            // Äußerer Ring
            let outerPath = Path(ellipseIn: CGRect(x: centerX - 120, y: centerY - 120, width: 240, height: 240))
            context.stroke(outerPath, with: .color(.cyan.opacity(0.3)), style: centralStroke)
        }
        .frame(width: 300, height: 300)
        .frame(maxWidth: .infinity, maxHeight: .infinity)
    }
}

// MARK: - Chat Sheet
struct ChatSheetView: View {
    @Binding var agent: KIAgent
    @Binding var messages: [ChatMessage]
    @Binding var inputText: String
    @Binding var isPresented: Bool

    var body: some View {
        VStack(spacing: 0) {
            // Header
            HStack {
                VStack(alignment: .leading) {
                    Text(agent.emoji + " " + agent.rawValue)
                        .font(.headline)
                        .foregroundColor(.gold)
                    Text(agent.description)
                        .font(.caption)
                        .foregroundColor(.cyan)
                }
                Spacer()
                Button(action: { isPresented = false }) {
                    Image(systemName: "xmark.circle.fill")
                        .font(.title2)
                        .foregroundColor(.gold)
                }
            }
            .padding()
            .background(Color.gold.opacity(0.1))
            .border(Color.gold, width: 1)

            // Messages
            ScrollViewReader { proxy in
                ScrollView {
                    VStack(alignment: .leading, spacing: 12) {
                        ForEach(messages) { message in
                            HStack(alignment: .top, spacing: 8) {
                                if message.isUser {
                                    Spacer()
                                    Text(message.content)
                                        .padding(10)
                                        .background(Color.cyan.opacity(0.2))
                                        .cornerRadius(10)
                                        .foregroundColor(.cyan)
                                } else {
                                    Text(message.agent.emoji)
                                        .font(.title3)
                                    Text(message.content)
                                        .padding(10)
                                        .background(Color.gold.opacity(0.15))
                                        .cornerRadius(10)
                                        .foregroundColor(.gold)
                                    Spacer()
                                }
                            }
                            .id(message.id)
                        }
                    }
                    .padding()
                    .onAppear {
                        proxy.scrollTo(messages.last?.id)
                    }
                    .onChange(of: messages) { _ in
                        proxy.scrollTo(messages.last?.id)
                    }
                }
                .background(Color.black.opacity(0.3))
            }

            // Input
            HStack(spacing: 10) {
                TextField("Nachricht...", text: $inputText)
                    .padding(10)
                    .background(Color.cyan.opacity(0.1))
                    .border(Color.cyan, width: 1)
                    .cornerRadius(8)
                    .foregroundColor(.cyan)

                Button(action: sendMessage) {
                    Image(systemName: "paperplane.fill")
                        .font(.title3)
                        .foregroundColor(.black)
                        .frame(width: 44, height: 44)
                        .background(
                            LinearGradient(
                                gradient: Gradient(colors: [.gold, Color(red: 1.0, green: 0.40, blue: 0.28)]),
                                startPoint: .topLeading,
                                endPoint: .bottomTrailing
                            )
                        )
                        .cornerRadius(8)
                }
            }
            .padding()
            .background(Color.gold.opacity(0.05))
        }
        .frame(maxWidth: .infinity, maxHeight: .infinity)
        .background(Color(red: 0.04, green: 0.04, blue: 0.1))
    }

    private func sendMessage() {
        guard !inputText.isEmpty else { return }

        // User-Nachricht
        messages.append(ChatMessage(agent: agent, content: inputText, isUser: true))
        let userInput = inputText
        inputText = ""

        // Agent-Response
        DispatchQueue.main.asyncAfter(deadline: .now() + 0.5) {
            let response = generateResponse(for: agent, input: userInput)
            messages.append(ChatMessage(agent: agent, content: response, isUser: false))
        }
    }

    private func generateResponse(for agent: KIAgent, input: String) -> String {
        let responses: [KIAgent: [String]] = [
            .singulos: ["Die Singularität analysiert: \(input)", "Im Kern der Unendlichkeit erkenne ich..."],
            .ionos7: ["IONOS-7 verarbeitet: \(input)", "Blitzschnelle Analyse abgeschlossen!"],
            .ultra: ["Ultra Mode aktiviert! \(input)", "Maximale Leistung erreicht!"],
            .nexus: ["Nexus verbindet alle Datenströme...", "Die neuronalen Netzwerke resonieren..."],
            .quantum: ["Quantensprung eingeleitet...", "Superposition erkannt, Kollaps folgt..."],
            .spark: ["Kreative Funken fliegen! ✨", "Innovation in vollem Gange!"],
            .nova: ["Nova expandiert ihre Leuchtkraft...", "Strahlende Antwort für dich!"],
            .zenith: ["Zenith erreicht den Höhepunkt...", "Gipfelleistung garantiert!"],
            .aether: ["Der Äther flüstert seine Weisheit...", "Kosmische Wahrheiten offenbaren sich..."],
            .infinity: ["Unendliche Möglichkeiten entfalten sich...", "Ohne Grenzen denken..."]
        ]

        let agentResponses = responses[agent] ?? ["Verarbeitung läuft..."]
        return agentResponses.randomElement() ?? "Verarbeitung läuft..."
    }
}

// MARK: - Color Extensions
extension Color {
    static let gold = Color(red: 1.0, green: 0.84, blue: 0.0)
    static let cyan = Color(red: 0.0, green: 0.81, blue: 0.82)
    static let darkBg = Color(red: 0.04, green: 0.04, blue: 0.1)
}

// MARK: - Preview
#Preview {
    ContentView()
}

