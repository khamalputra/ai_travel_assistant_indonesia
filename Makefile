.PHONY: install run clean test format lint docker-build docker-run help

# Variables
PYTHON := python3
PIP := pip3
STREAMLIT := streamlit
APP_FILE := ai_travel_assistant.py
IMAGE_NAME := travel-assistant
CONTAINER_NAME := travel-assistant-container

# Default target
help:
	@echo "🤖 AI Travel Assistant - Available Commands:"
	@echo ""
	@echo "📦 Setup & Installation:"
	@echo "  make install         Install dependencies"
	@echo "  make install-dev     Install dev dependencies"
	@echo ""
	@echo "🚀 Running:"
	@echo "  make run             Run Streamlit app"
	@echo "  make run-dev         Run with file watching"
	@echo ""
	@echo "🧪 Testing & Quality:"
	@echo "  make test            Run basic tests"
	@echo "  make format          Format code with Black"
	@echo "  make lint            Run linting with flake8"
	@echo "  make check           Run all quality checks"
	@echo ""
	@echo "🐳 Docker:"
	@echo "  make docker-build    Build Docker image"
	@echo "  make docker-run      Run Docker container"
	@echo "  make docker-stop     Stop Docker container"
	@echo ""
	@echo "🧹 Cleanup:"
	@echo "  make clean           Clean cache and temp files"
	@echo "  make clean-all       Clean everything including venv"

# Setup and Installation
install:
	@echo "📦 Installing dependencies..."
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements.txt

install-dev:
	@echo "📦 Installing development dependencies..."
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements.txt
	$(PIP) install pytest black flake8 bandit

# Running the application
run:
	@echo "🚀 Starting Travel Assistant..."
	$(STREAMLIT) run $(APP_FILE)

run-dev:
	@echo "🚀 Starting Travel Assistant (Development Mode)..."
	$(STREAMLIT) run $(APP_FILE) --server.fileWatcherType poll

# Testing and Quality
test:
	@echo "🧪 Running basic functionality tests..."
	$(PYTHON) -c "
	import sys
	try:
	    from $(basename $(APP_FILE) .py) import check_libraries, get_basic_response
	    print('✅ Import test passed')
	    
	    # Test basic response
	    response = get_basic_response('test budget')
	    assert len(response) > 0
	    print('✅ Basic response test passed')
	    
	    print('✅ All tests passed!')
	except Exception as e:
	    print(f'❌ Test failed: {e}')
	    sys.exit(1)
	"

format:
	@echo "🎨 Formatting code with Black..."
	black $(APP_FILE)
	@echo "✅ Code formatting complete"

lint:
	@echo "🔍 Running linting checks..."
	flake8 $(APP_FILE) --max-line-length=100 --extend-ignore=E203,W503
	@echo "✅ Linting complete"

security:
	@echo "🔒 Running security scan..."
	bandit -r . -f json -o bandit-report.json
	@echo "✅ Security scan complete (check bandit-report.json)"

check: format lint test security
	@echo "✅ All quality checks passed!"

# Docker commands
docker-build:
	@echo "🐳 Building Docker image..."
	docker build -t $(IMAGE_NAME):latest .

docker-run: docker-build
	@echo "🐳 Running Docker container..."
	docker run -d \
		--name $(CONTAINER_NAME) \
		-p 8501:8501 \
		--env-file .env \
		$(IMAGE_NAME):latest

docker-stop:
	@echo "🛑 Stopping Docker container..."
	docker stop $(CONTAINER_NAME) || true
	docker rm $(CONTAINER_NAME) || true

docker-logs:
	@echo "📋 Showing Docker logs..."
	docker logs -f $(CONTAINER_NAME)

# Docker Compose commands
compose-up:
	@echo "🐳 Starting with Docker Compose..."
	docker-compose up -d

compose-down:
	@echo "🛑 Stopping Docker Compose..."
	docker-compose down

compose-dev:
	@echo "🐳 Starting development environment..."
	docker-compose --profile dev up

# Cleanup
clean:
	@echo "🧹 Cleaning cache and temporary files..."
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete
	find . -type f -name "*.pyd" -delete
	find . -type f -name ".coverage" -delete
	find . -type d -name "*.egg-info" -exec rm -rf {} +
	rm -rf .pytest_cache/
	rm -rf .mypy_cache/
	rm -rf build/
	rm -rf dist/
	rm -f bandit-report.json

clean-all: clean
	@echo "🧹 Cleaning everything including virtual environment..."
	rm -rf venv/
	rm -rf env/

# Development helpers
requirements:
	@echo "📋 Generating requirements.txt from current environment..."
	pip freeze > requirements.txt

env-example:
	@echo "📝 Creating .env.example from current .env..."
	sed 's/=.*/=your_value_here/' .env > .env.example

# Git helpers
git-setup:
	@echo "🔧 Setting up git hooks..."
	echo "#!/bin/sh\nmake format lint" > .git/hooks/pre-commit
	chmod +x .git/hooks/pre-commit

# Quick development setup
dev-setup: install-dev env-example git-setup
	@echo "🎉 Development environment setup complete!"
	@echo "📝 Don't forget to:"
	@echo "  1. Copy .env.example to .env"
	@echo "  2. Add your GOOGLE_API_KEY to .env"
	@echo "  3. Run 'make run' to start the app"

# Production deployment helpers
deploy-check: check
	@echo "✅ Ready for deployment!"

# Show project info
info:
	@echo "ℹ️  Project Information:"
	@echo "📁 Project: AI Travel Assistant Indonesia"
	@echo "🐍 Python: $$($(PYTHON) --version)"
	@echo "📦 Pip: $$($(PIP) --version)"
	@echo "🎯 Streamlit: $$($(STREAMLIT) version 2>/dev/null || echo 'Not installed')"
	@echo "📂 Working Directory: $$(pwd)"
	@echo "📋 Files:"
	@ls -la $(APP_FILE) requirements.txt README.md 2>/dev/null || echo "  Some files missing"
