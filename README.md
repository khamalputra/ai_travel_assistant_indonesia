# 🤖 AI Travel Assistant Indonesia

![Python](https://img.shields.io/badge/python-v3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/streamlit-v1.28+-red.svg)
![LangChain](https://img.shields.io/badge/langchain-v0.2+-green.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

Asisten travel AI yang didukung oleh LangChain dan Google Gemini 2.0 Flash, dirancang khusus untuk traveler Indonesia yang ingin menjelajahi Asia Tenggara.

## ✨ Features

- 🤖 **AI-Powered Responses** - Menggunakan Google Gemini 2.0 Flash untuk jawaban yang cerdas dan personal
- 💬 **Smart Chat Interface** - Antarmuka chat yang responsif dan user-friendly
- 🎯 **Quick Actions** - Tombol cepat untuk pertanyaan umum travel
- 💰 **Budget Planning** - Estimasi budget dalam Rupiah untuk berbagai destinasi
- 🌤️ **Weather Information** - Info cuaca terkini untuk destinasi Asia Tenggara
- ✈️ **Flight Search** - Rekomendasi penerbangan murah dari Indonesia
- 📋 **Itinerary Planning** - Bantuan perencanaan perjalanan yang detail
- 🏨 **Accommodation Tips** - Saran akomodasi sesuai budget

## 🎯 Target Destinasi

- 🇮🇩 **Indonesia** - Bali, Yogyakarta, Lombok, dan lainnya
- 🇸🇬 **Singapore** - Budget travel dan luxury options
- 🇹🇭 **Thailand** - Bangkok, Phuket, Chiang Mai
- 🇲🇾 **Malaysia** - Kuala Lumpur, Penang, Langkawi
- 🇻🇳 **Vietnam** - Ho Chi Minh, Hanoi, Da Nang
- 🇵🇭 **Philippines** - Manila, Boracay, Palawan

## 🚀 Quick Start

### Prerequisites

- Python 3.8 atau lebih tinggi
- Google Gemini API Key (gratis di [Google AI Studio](https://makersuite.google.com/app/apikey))

### Installation

1. **Clone repository:**
   ```bash
   git clone https://github.com/yourusername/ai-travel-assistant-indonesia.git
   cd ai-travel-assistant-indonesia
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run application:**
   ```bash
   streamlit run travel_assistant_with_langchain.py
   ```

4. **Access aplikasi:**
   - Buka browser ke `http://localhost:8501`
   - Masukkan Google Gemini API Key di sidebar
   - Mulai bertanya tentang travel!

## 🔧 Configuration

### API Key Setup

1. Kunjungi [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Buat API key baru (gratis)
3. Masukkan API key di sidebar aplikasi
4. Nikmati fitur AI yang lengkap!

### Environment Variables (Optional)

Buat file `.env` untuk menyimpan API key:
```env
GOOGLE_API_KEY=your_gemini_api_key_here
```

## 💻 Usage Examples

### Basic Questions
```
🗣️ User: "Flight murah Jakarta ke Bali minggu depan"
🤖 AI: [Memberikan rekomendasi airline, harga, dan tips booking]

🗣️ User: "Budget backpacking Thailand 1 minggu"  
🤖 AI: [Detail budget breakdown, tips hemat, itinerary sederhana]

🗣️ User: "Cuaca di Singapore bulan Maret"
🤖 AI: [Prakiraan cuaca, tips packing, aktivitas yang cocok]
```

### Advanced Planning
```
🗣️ User: "Planning honeymoon ke Bali 5 hari budget 15 juta"
🤖 AI: [Itinerary detail, hotel romantis, aktivitas couple, breakdown budget]

🗣️ User: "Backpacking Vietnam 2 minggu, suka kuliner dan sejarah"
🤖 AI: [Route planning, food recommendations, historical sites, budget tips]
```

## 🛠️ Tech Stack

- **Frontend:** Streamlit
- **AI Framework:** LangChain
- **LLM:** Google Gemini 2.0 Flash
- **Language:** Python 3.8+
- **Memory:** RunnableWithMessageHistory (LangChain modern approach)

## 📁 Project Structure

```
ai-travel-assistant-indonesia/
├── travel_assistant_with_langchain.py    # Main application
├── requirements.txt                       # Python dependencies
├── README.md                             # Project documentation
├── LICENSE                               # MIT License
├── .env.example                          # Environment variables example
├── .gitignore                           # Git ignore rules
├── setup.py                             # Package setup (optional)
└── docs/                                # Documentation
    ├── installation.md                  # Detailed installation guide
    ├── api_setup.md                     # API key setup guide
    └── contributing.md                  # Contribution guidelines
```

## 🤝 Contributing

Kontribusi sangat welcome! Lihat [CONTRIBUTING.md](docs/contributing.md) untuk guidelines.

### Development Setup

1. Fork repository
2. Create feature branch: `git checkout -b feature/amazing-feature`
3. Commit changes: `git commit -m 'Add amazing feature'`
4. Push branch: `git push origin feature/amazing-feature`
5. Submit Pull Request

## 🐛 Known Issues & Solutions

### Common Problems:

1. **LangChain Deprecation Warnings**
   - ✅ **Fixed:** Updated to use modern LangChain patterns
   - Uses `RunnableWithMessageHistory` instead of `ConversationChain`

2. **API Key Issues**
   - Pastikan API key valid dan aktif
   - Check quota limit di Google AI Studio
   - Restart aplikasi setelah input API key

3. **Import Errors**
   - Run: `pip install --upgrade -r requirements.txt`
   - Pastikan Python version 3.8+

## 📊 Performance

- **Response Time:** < 3 detik untuk pertanyaan standar
- **Memory Usage:** ~100MB RAM untuk chat session normal  
- **API Calls:** Optimized untuk minimize cost
- **Offline Mode:** Basic responses tersedia tanpa API key

## 🔒 Privacy & Security

- API key disimpan local di session (tidak tersimpan permanen)
- Chat history tidak dikirim ke server external
- Tidak ada data personal yang disimpan
- GDPR compliant design

## 📈 Roadmap

### Version 2.0
- [ ] Database integration untuk menyimpan preferensi
- [ ] Multi-language support (English, Mandarin)
- [ ] Real-time flight price tracking
- [ ] Integration dengan booking platform

### Version 2.1  
- [ ] Voice input/output
- [ ] Image recognition untuk destinasi
- [ ] Weather alerts
- [ ] Travel community features

## 📄 License

Project ini menggunakan MIT License - lihat file [LICENSE](LICENSE) untuk detail.

## 👨‍💻 Author

**Your Name**
- GitHub: [@khamalputra](https://github.com/khamalputra)
- Email: khamalade@gmail.com
- LinkedIn: [khamalputra](https://linkedin.com/in/adekhameliaputra/)

## 🙏 Acknowledgments

- [LangChain](https://langchain.com/) - Framework AI yang powerful
- [Google Gemini](https://ai.google.dev/) - Large Language Model  
- [Streamlit](https://streamlit.io/) - Framework web app yang mudah
- Travel community Indonesia - Inspirasi dan feedback

## 📞 Support

Jika ada pertanyaan atau issue:

1. Check [Issues](https://github.com/khamalputra/ai-travel-assistant-indonesia/issues) yang sudah ada
2. Buat issue baru dengan label yang sesuai
3. Join discussion di [Discussions](https://github.com/khamalputra/ai-travel-assistant-indonesia/discussions)

---

⭐ **Star project ini jika bermanfaat!**

Made with ❤️ for Indonesian travelers
