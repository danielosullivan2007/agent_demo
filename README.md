# AI Agent Demo System

A sophisticated multi-agent collaboration demo featuring real-time visualization, tool integration, and live workflow orchestration.

## 🚀 Features

- **Multi-Agent Collaboration**: Support, Manager, Analyst, Security, and ML Expert agents working together
- **Real-Time Visualization**: Dynamic graph showing agent states and tool usage
- **MCP Server Integration**: Customer Analytics, SEMGREP Security, Model Testing Suite, and **JIRA Cloud**
- **Live Tool Execution**: Watch agents use tools with real-time feedback
- **Professional UI**: Dark theme with neon colors, floating status, and clean controls
- **Human-in-the-Loop**: Approval workflows for critical decisions

## 🎯 Perfect for Product Demonstrations

This demo showcases how AI agents can collaborate to solve complex business problems, complete with:
- Professional ticket management via JIRA integration
- Security scanning and approval workflows
- Data analysis and ML model validation
- Real-time status updates and progress tracking

## 🔧 Quick Start

1. **Install Dependencies**:
   ```bash
   npm install
   ```

2. **Configure Environment** (Optional):
   ```bash
   cp .env.example .env.local
   # Edit .env.local with your API keys
   ```

3. **Start Development Server**:
   ```bash
   npm run dev
   ```

4. **Open Demo**: Navigate to `http://localhost:5173`

## 🎫 JIRA Cloud Integration

### Connect Your Real JIRA Instance

The demo can create, update, and close real JIRA tickets! See **[JIRA_SETUP.md](./JIRA_SETUP.md)** for detailed setup instructions.

**Quick Setup**:
1. Generate JIRA API token at [Atlassian Account Settings](https://id.atlassian.com/manage-profile/security/api-tokens)
2. Configure `.env.local`:
   ```env
   VITE_JIRA_BASE_URL=https://yourcompany.atlassian.net
   VITE_JIRA_EMAIL=your.email@company.com
   VITE_JIRA_API_TOKEN=your_api_token_here
   VITE_JIRA_PROJECT_KEY=YOUR_PROJECT_KEY
   ```
3. Restart the server and watch real tickets get created!

**Without JIRA**: The demo works perfectly with mock responses if JIRA isn't configured.

## 🤖 OpenAI Integration

For real AI agent responses, add your OpenAI API key:
```env
VITE_OPENAI_API_KEY=your_openai_api_key_here
```

**Without OpenAI**: The demo uses intelligent mock responses that showcase the agent collaboration perfectly.

## 🛠 MCP Servers Simulated

- **🎫 JIRA Cloud**: Real ticket management (when configured) or mock ticket operations
- **🗄️ Customer Analytics**: Customer segmentation and behavior analysis
- **🌍 SEMGREP Security**: Code security scanning and vulnerability assessment
- **🤖 Model Testing Suite**: ML model validation, A/B testing, and deployment readiness

## 🎮 How to Use

1. **Start Demo**: Click the green "Start Demo" button
2. **Watch Collaboration**: Agents automatically coordinate to solve the customer issue
3. **Human Approval**: When prompted, click "✅ Human in the Loop Approval" for security reviews
4. **View Progress**: Monitor real-time status in the floating display
5. **Check JIRA**: If configured, see real tickets being created and managed
6. **Toggle Chat**: Click "💬 Show Chat History" to see detailed agent conversations

## 🎨 Architecture

- **React + TypeScript**: Modern frontend with type safety
- **React Flow**: Professional graph visualization
- **Vite**: Fast development and building
- **Agent Manager**: Orchestrates AI agent execution and tool calls
- **Demo Workflow**: Configurable multi-step collaboration scenarios
- **Real APIs**: Optional integration with JIRA Cloud and OpenAI

This demo represents a production-ready approach to multi-agent systems with real tool integration and professional presentation suitable for client demonstrations and product showcases.
```

You can also install [eslint-plugin-react-x](https://github.com/Rel1cx/eslint-react/tree/main/packages/plugins/eslint-plugin-react-x) and [eslint-plugin-react-dom](https://github.com/Rel1cx/eslint-react/tree/main/packages/plugins/eslint-plugin-react-dom) for React-specific lint rules:

```js
// eslint.config.js
import reactX from 'eslint-plugin-react-x'
import reactDom from 'eslint-plugin-react-dom'

export default tseslint.config([
  globalIgnores(['dist']),
  {
    files: ['**/*.{ts,tsx}'],
    extends: [
      // Other configs...
      // Enable lint rules for React
      reactX.configs['recommended-typescript'],
      // Enable lint rules for React DOM
      reactDom.configs.recommended,
    ],
    languageOptions: {
      parserOptions: {
        project: ['./tsconfig.node.json', './tsconfig.app.json'],
        tsconfigRootDir: import.meta.dirname,
      },
      // other options...
    },
  },
])
```
