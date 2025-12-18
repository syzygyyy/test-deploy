# Python Logger App

Simple Python application that continuously prints log messages for testing Hostany deployment.

## Features

- 🔄 Continuous logging
- 📊 Multiple log levels (INFO, WARNING, ERROR)
- ⏰ Timestamps on every log
- 🎲 Random log generation
- 💚 Graceful shutdown

## Files

```
python/
├── app.py              # Main application
├── requirements.txt    # Dependencies (none for this app)
└── README.md          # This file
```

## Running Locally

```bash
python app.py
```

Output example:
```
======================================================================
🚀 Python Logger App Started
======================================================================
[2025-12-17 10:30:45] INFO: Initialization complete
[2025-12-17 10:30:45] INFO: Starting continuous logging...
======================================================================
[2025-12-17 10:30:47] INFO: Application is running smoothly
[2025-12-17 10:30:50] WARNING: High memory usage detected
[2025-12-17 10:30:53] INFO: Processing data batch
[2025-12-17 10:30:56] INFO: Health check passed
...
```

## Testing with Hostany

### Step 1: Create ZIP file

**Option A: Using PowerShell (Windows)**
```powershell
cd D:\code\hostany\example
Compress-Archive -Path python\* -DestinationPath python-logger-app.zip
```

**Option B: Using Git Bash / WSL**
```bash
cd /d/code/hostany/example
zip -r python-logger-app.zip python/
```

**Option C: Using 7-Zip / WinRAR**
- Right-click on `python` folder
- Select "Add to archive..."
- Create `python-logger-app.zip`

### Step 2: Deploy to Hostany

1. Start Hostany frontend: http://localhost:3000
2. Click "Deploy New Bot (ZIP)"
3. Upload `python-logger-app.zip`
4. Wait for deployment (2-5 minutes)
5. View real-time logs!

### Expected Deployment Behavior

**AI Analysis:**
- ✅ Detects: Python project
- ✅ Entry point: `app.py`
- ✅ Dependencies: None (standard library only)

**Dockerfile Generated:**
```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 8000
CMD ["python", "app.py"]
```

**Pod Status:**
- Starts as `Pending`
- Changes to `Running` once deployed
- Continuously prints logs

## Log Patterns

The app generates three types of logs:

- **INFO (70%)**: Normal operations
- **WARNING (20%)**: Potential issues
- **ERROR (10%)**: Failures

Logs are printed every 2-5 seconds with random messages.

## Stopping the App

**Locally:**
Press `Ctrl+C` to stop gracefully

**In Kubernetes:**
Delete the bot through Hostany UI or:
```bash
kubectl delete pod bot-<bot-id> -n hostany-bots
```

## Requirements

- Python 3.7+
- No external dependencies

## Use Cases

- ✅ Testing Hostany deployment
- ✅ Verifying log streaming
- ✅ Demonstrating Pod lifecycle
- ✅ Learning Kubernetes basics
- ✅ CI/CD pipeline testing

## Customization

Want to modify the logs? Edit `app.py`:

```python
# Change log frequency (line 72)
sleep_time = random.uniform(1, 3)  # Faster logs

# Add custom log messages (lines 20-37)
log_types = [
    ('INFO', ['Your custom message here']),
    ...
]
```

## Troubleshooting

**Problem**: App doesn't start

**Solution**: Check Python version
```bash
python --version  # Should be 3.7+
```

**Problem**: Can't create ZIP

**Solution**: Use absolute paths or cd to parent directory

---

Made with ❤️ for testing Hostany deployments
