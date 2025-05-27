# 📰 MagPi Downloader

A Python script to batch download all [Raspberry Pi MagPi](https://magazine.raspberrypi.com/) magazine issues (1–153) in PDF format.

## ✅ Features

- Downloads all available MagPi PDFs (Issues 1–153)
- Skips already-downloaded files
- Retries on download failures (up to 3 times)
- Shows live progress with `tqdm`

## 📦 Requirements

- Python 3.7+
- Virtual environment recommended

Install dependencies:

```bash
pip install -r requirements.txt
```

## 🚀 Usage

### 1. Clone the repository and set up your environment

```bash
git clone https://github.com/your-username/rpipress-downloader.git
cd rpipress-downloader
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 2. Run the script

```bash
python download_magpi.py
```

You can also make it directly executable by adding a shebang and running:

```bash
chmod +x download_magpi.py
./download_magpi.py
```

## 📁 Output

Downloaded issues will be saved to:

```
MagPi_Issues/
├── MagPi_Issue_1.pdf
├── MagPi_Issue_2.pdf
├── ...
```

## 🧰 Customization

- Modify `total_issues` in the script if more issues are published.
- Add logic to zip the folder or log results to CSV if needed.

## 🧑‍💻 License

MIT License (or your preferred open source license)

---

Built with ❤️ by [@mschemerii](mailto:mschemerii@gmail.com)
