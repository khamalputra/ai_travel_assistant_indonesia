# 🤝 Contributing to AI Travel Assistant Indonesia

Terima kasih telah tertarik berkontribusi! Project ini welcome untuk semua level developer.

## 🎯 Ways to Contribute

### 1. 🐛 Bug Reports
- Gunakan GitHub Issues dengan label `bug`
- Include langkah reproduce error
- Screenshot atau video jika memungkinkan
- Environment details (OS, Python version, dll)

### 2. ✨ Feature Requests  
- Buat issue dengan label `enhancement`
- Jelaskan use case dan benefit
- Mockup atau wireframe jika ada

### 3. 💻 Code Contributions
- Fork repository
- Create feature branch
- Implement changes
- Submit Pull Request

### 4. 📝 Documentation
- Improve README
- Add code comments
- Create tutorials
- Translate docs

## 🛠️ Development Setup

### Prerequisites
```bash
Python 3.8+
Git
Google Gemini API Key
```

### Local Development
```bash
# 1. Fork dan clone repo
git clone https://github.com/yourusername/ai-travel-assistant-indonesia.git
cd ai-travel-assistant-indonesia

# 2. Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
# atau
venv\Scripts\activate  # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Setup environment
cp .env.example .env
# Edit .env dengan API key Anda

# 5. Run aplikasi
streamlit run travel_assistant_with_langchain.py
```

## 📋 Pull Request Process

### Before Submit PR:

1. **Test thoroughly:**
   ```bash
   # Test dengan dan tanpa API key
   # Test semua quick action buttons
   # Test chat functionality
   ```

2. **Code quality check:**
   ```bash
   # Format code
   black travel_assistant_with_langchain.py
   
   # Check for issues
   flake8 travel_assistant_with_langchain.py
   ```

3. **Update documentation** jika diperlukan

### PR Guidelines:

- **Title:** Descriptive dan clear
- **Description:** Jelaskan changes dan reasoning
- **Screenshots:** Untuk UI changes
- **Testing:** List test cases yang sudah dilakukan

## 🎨 Code Style

### Python Style Guide
- Follow PEP 8
- Use Black for formatting
- Max line length: 100 characters
- Descriptive variable names

### Example:
```python
# Good ✅
def setup_langchain_chain(api_key: str) -> bool:
    """Setup LangChain conversation chain with Gemini."""
    try:
        llm = ChatGoogleGenerativeAI(
            model="gemini-2.0-flash-exp",
            google_api_key=api_key,
            temperature=0.7
        )
        return True
    except Exception as e:
        st.error(f"Setup failed: {e}")
        return False

# Avoid ❌  
def setup(k):
    l = ChatGoogleGenerativeAI(model="gemini-2.0-flash-exp",google_api_key=k,temperature=0.7)
    return True
```

### Streamlit Best Practices
- Use session state properly
- Handle errors gracefully  
- Responsive design
- Clear user feedback
- Optimize performance

## 🐛 Issue Labels

- `bug` - Something tidak bekerja
- `enhancement` - Feature request
- `documentation` - Docs improvements
- `good first issue` - Good untuk newcomers
- `help wanted` - Butuh bantuan community
- `question` - Pertanyaan general

## 📝 Commit Message Format

```
type(scope): description

[optional body]

[optional footer]
```

### Types:
- `feat` - New feature
- `fix` - Bug fix
- `docs` - Documentation
- `style` - Formatting changes
- `refactor` - Code refactoring
- `test` - Adding tests
- `chore` - Maintenance

### Examples:
```
feat(chat): add voice input functionality

fix(api): handle gemini rate limit errors

docs(readme): update installation instructions
```

## 🔍 Testing Guidelines

### Manual Testing Checklist:
- [ ] App starts without errors
- [ ] Basic mode works (no API key)
- [ ] AI mode works (with API key)
- [ ] All quick action buttons functional
- [ ] Chat input/output works
- [ ] Clear chat works
- [ ] Responsive design on mobile

### Test Cases:
```python
# Test basic responses
test_input = "flight murah jakarta bali"
expected_keywords = ["jakarta", "bali", "flight", "rp"]

# Test error handling  
test_invalid_api_key = "invalid_key_123"
expected_error = "API key error"
```

## 🌟 Feature Development Priority

### High Priority:
1. Bug fixes dan stability
2. Performance improvements
3. Better error handling
4. Mobile responsiveness

### Medium Priority:
1. New travel destinations
2. Enhanced AI responses
3. Better UI/UX
4. Additional quick actions

### Low Priority:
1. Advanced features
2. Integrations
3. Analytics
4. Multi-language

## 💬 Communication

### Where to Ask Questions:
- **General questions:** GitHub Discussions
- **Bug reports:** GitHub Issues
- **Feature requests:** GitHub Issues
- **Development help:** GitHub Discussions

### Response Time:
- Issues: 1-3 hari
- Pull Requests: 2-5 hari  
- Discussions: 1-2 hari

## 🏆 Recognition

Contributors akan diakui di:
- README.md contributors section
- Release notes
- Special mentions untuk major contributions

## 📚 Resources

### LangChain:
- [LangChain Documentation](https://python.langchain.com/)
- [Migration Guide](https://python.langchain.com/docs/versions/migrating_memory/)

### Streamlit:
- [Streamlit Documentation](https://docs.streamlit.io/)
- [Component Gallery](https://streamlit.io/gallery)

### Google Gemini:
- [Gemini API Docs](https://ai.google.dev/docs)
- [API Key Setup](https://makersuite.google.com/app/apikey)

---

**Happy Contributing! 🎉**

Setiap kontribusi, sekecil apapun, sangat dihargai! ⭐
