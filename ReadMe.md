# LLM Chat Application

A scalable chat application built with FastAPI and Redis that integrates GPT-J for intelligent conversation handling. The system uses Redis streams for message queuing and processing, enabling real-time chat functionality with AI responses.

## 🏗️ Architecture

The application consists of two main components:

- **Server** (`server/main.py`): FastAPI web server that handles HTTP requests and manages chat routes
- **Worker** (`worker/main.py`): Background worker that processes messages from Redis streams and generates AI responses using GPT-J

## 📋 Features

- ✅ Real-time chat functionality
- ✅ Redis-based message streaming and caching
- ✅ GPT-J integration for AI responses
- ✅ Chat history management
- ✅ Scalable worker architecture
- ✅ Development and production environments

## 🛠️ Technology Stack

- **Backend**: FastAPI (Python)
- **Message Queue**: Redis Streams
- **Caching**: Redis with ReJSON
- **AI Model**: GPT-J
- **ASGI Server**: Uvicorn
- **Environment Management**: python-dotenv

## 📦 Installation

### Prerequisites

- Python 3.8+
- Redis server
- pip or poetry for package management

### Setup

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd llm-chat-application
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   Create a `.env` file in the root directory:
   ```env
   APP_ENV=development
   REDIS_HOST=localhost
   REDIS_PORT=6379
   REDIS_PASSWORD=
   ```

4. **Start Redis server**
   ```bash
   redis-server
   ```

## 🚀 Usage

### Starting the Application

1. **Start the FastAPI server**
   ```bash
   cd server
   python main.py
   ```
   The server will start on `http://0.0.0.0:3500` in development mode.

2. **Start the worker process**
   ```bash
   cd worker
   python main.py
   ```

### Testing the Setup

Visit `http://localhost:3500/test` to verify the server is running. You should see:
```json
{"msg": "Mein chea chalan"}
```

## 🔧 Configuration

### Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `APP_ENV` | Application environment (development/production) | development |
| `REDIS_HOST` | Redis server host | localhost |
| `REDIS_PORT` | Redis server port | 6379 |
| `REDIS_PASSWORD` | Redis password (if required) | - |

### Development vs Production

- **Development**: Runs with auto-reload and 4 workers
- **Production**: Custom configuration (currently not implemented)

## 📡 API Endpoints

### Test Endpoint
```
GET /test
```
Returns a simple test message to verify server status.

### Chat Endpoints
The chat functionality is handled through the chat router (implementation in `src/routes/chat`).

## 🔄 How It Works

1. **Message Flow**:
   - User sends a message via the chat API
   - Message is added to Redis stream (`message_channel`)
   - Worker consumes the message from the stream
   - Worker processes the message and generates AI response using GPT-J
   - Response is cached in Redis and returned to user

2. **Chat History**:
   - Last 4 messages are used as context for generating responses
   - Chat history is stored in Redis with ReJSON for efficient retrieval

3. **Message Processing**:
   - Each message is associated with a token for session management
   - Messages are processed sequentially to maintain conversation flow
   - Processed messages are deleted from the queue

## 🏃‍♂️ Development

### Project Structure
```
├── server/
│   └── main.py          # FastAPI server
├── worker/
│   └── main.py          # Background worker
├── src/
│   ├── routes/
│   │   └── chat.py      # Chat API routes
│   ├── redis/
│   │   ├── config.py    # Redis configuration
│   │   ├── cache.py     # Cache operations
│   │   ├── stream.py    # Stream consumer
│   │   └── producer.py  # Stream producer
│   ├── model/
│   │   └── gptj.py      # GPT-J model integration
│   └── schema/
│       └── chat.py      # Message schemas
├── .env                 # Environment variables
└── requirements.txt     # Dependencies
```

### Running in Development Mode

The application automatically runs in development mode when `APP_ENV=development`:
- Auto-reload enabled
- 4 worker processes
- Detailed logging

## 🔍 Monitoring

### Worker Logs
The worker provides console output for monitoring:
- "Stream consumer started"
- "Stream waiting for new messages"
- Token and message processing information

### Health Check
Use the `/test` endpoint to verify server health.

## 🐛 Troubleshooting

### Common Issues

1. **Redis Connection Failed**
   - Ensure Redis server is running
   - Check Redis host/port configuration
   - Verify Redis password if authentication is enabled

2. **Worker Not Processing Messages**
   - Check Redis stream configuration
   - Verify message format in the stream
   - Ensure GPT-J model is properly initialized

3. **Server Not Starting**
   - Check if port 3500 is available
   - Verify all dependencies are installed
   - Check environment variables

### Debug Mode

Set `APP_ENV=development` and check console logs for detailed information about:
- Message processing
- Redis operations
- GPT-J model responses

## 📈 Performance Considerations

- The worker processes messages sequentially for conversation coherence
- Chat history is limited to last 4 messages for optimal response generation
- Redis streams provide efficient message queuing and processing
- Multiple server workers (4) handle concurrent HTTP requests

## 🔒 Security Notes

- Implement proper authentication for production use
- Secure Redis with password authentication
- Validate and sanitize user inputs
- Consider rate limiting for API endpoints

## 📄 License

[Add your license information here]

## 🤝 Contributing

[Add contribution guidelines here]

## 📞 Support

[Add support contact information here]