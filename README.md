# 🐉 Zahard's Ultimate CTF Zsh Configuration

A highly customized **Zsh configuration** designed for **Kali Linux**.
This setup is optimized for **CTF (Capture The Flag)** players, **Pwn/Reverse Engineers**, and those who appreciate a "Wibu-style" aesthetic with high-performance terminal tools.

## ✨ Key Features

* **Visuals:** Integrated `neofetch` with Sixel image support (Waifu), dynamic `oh-my-posh` theme, and desktop Shimeji pets.
* **Workflow:** seamless Clipboard synchronization via SSH (OSC 52), smart directory navigation (`zoxide`), and syntax highlighting.
* **CTF Arsenal:**
    * **Pwn:** `bininfo` (Auto-analysis), `gdbpwn`, `plzsh` (TTY upgrade).
    * **Web/Net:** One-liner servers (`webup`, `ftpup`, `smbup`), fast scanning wrappers (`mscanz`).
    * **Dev:** Virtualenv management (`qvenv`), Docker shortcuts.

---

## 📦 1. Prerequisites & Dependencies

To ensure all aliases and functions work correctly, you must install the following packages.

### A. System Packages (APT)
Run this command to install core utilities, Python environment, and UI tools:

```bash
sudo apt update
sudo apt install -y zsh git curl wget unzip bat eza fzf ripgrep fd-find \
    zoxide neofetch wmctrl libsixel-bin python3-venv python3-pip \
    proxychains4 sshpass xfreerdp net-tools colordiff 7zip unrar cabextract \
    libnotify-bin xclip
```

### B. Python Tools (PIP)
Install essential libraries for the CTF scripts and visual tools:

```bash
pip install --break-system-packages pyftpdlib impacket wsgidav pwn pwntools \
    google-generativeai colorama
```

### C. Assets (Fonts & Images)
1.  **Nerd Fonts (Required):** Install [JetBrainsMono Nerd Font](https://www.nerdfonts.com/) to avoid broken icons.
2.  **Neofetch Image:** Place your desired image at `~/Pictures/NGU1.png`.
3.  **Themes:** Download `lambdageneration.omp.json` to `~/.oh-my-posh/themes/`.

---

## 🛠️ 2. Installation Guide

### Step 1: Install Zsh Frameworks
```bash
# 1. Install Oh My Zsh
sh -c "$(curl -fsSL [https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh](https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh))"

# 2. Install Oh My Posh (Prompt Theme)
sudo wget [https://github.com/JanDeDobbeleer/oh-my-posh/releases/latest/download/posh-linux-amd64](https://github.com/JanDeDobbeleer/oh-my-posh/releases/latest/download/posh-linux-amd64) -O /usr/local/bin/oh-my-posh
sudo chmod +x /usr/local/bin/oh-my-posh

# 3. Install Zsh Plugins (Autosuggestions & Highlighting)
git clone [https://github.com/zsh-users/zsh-autosuggestions](https://github.com/zsh-users/zsh-autosuggestions) ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions
sudo apt install zsh-syntax-highlighting
```

### Step 2: Configure Custom Scripts
This config relies on a custom Python script for `ls` display.
* **Action:** Ensure you have the `ltable.py` script saved at `~/.ltable.py`.
* *Alternative:* If you don't have this script, comment out the line `alias ls='python3 ~/.ltable.py'` in the config file.

### Step 3: Apply the Configuration
1.  Open your current config: `nano ~/.zshrc`
2.  Paste the content of **Zahard's Config** into the file.
3.  Save and reload:
    ```bash
    source ~/.zshrc
    ```

---

## 🚀 3. Command Cheatsheet

### 🎨 Visual & System
| Command | Description |
| :--- | :--- |
| **`c`** | Clear screen + Neofetch (Displays `~/Pictures/NGU1.png` via Sixel). |
| **`shimeji`** | Spawns Shimeji characters (978, 494...) on your desktop. |
| **`ccfg`** | Copies the content of `.zshrc` to Windows Clipboard (OSC 52). |
| **`sshup`** | Copies the SSH connect command for this machine to Windows Clipboard. |
| **`niggamode`** | **WARNING:** Switches to TTY3 (Black CLI interface). |
| **`godmode`** | Returns to GUI (TTY2). |

### 📂 File Navigation
| Command | Description |
| :--- | :--- |
| **`ls` / `ll`** | Enhanced list view using `ltable.py` or `eza`. |
| **`cat` / `p`** | View file content with syntax highlighting (uses `bat` theme Dracula). |
| **`extract <file>`** | Universal extractor for `.tar`, `.zip`, `.rar`, `.7z`, `.exe`. |
| **`ff <name>`** | Find files instantly using `fd` + `fzf`. |
| **`fstr <text>`** | Find text inside files using `ripgrep` + `fzf`. |
| **`mkcd <dir>`** | Create a directory and `cd` into it immediately. |

### 💀 CTF: Pwn & Reverse Engineering
| Command | Description |
| :--- | :--- |
| **`bininfo <bin>`** | **The Ultimate Analysis Tool:** Checks file type, security protections (Checksec), LDD, and finds offsets for `system`, `/bin/sh`, and `pop rdi` gadget. |
| **`gdbpwn`** | Launches GDB in quiet mode. |
| **`plzsh`** | Upgrades a reverse shell to a fully interactive TTY (fixes arrow keys, Ctrl+C). |
| **`tplt`** | Generates a `pwntools` exploit template. |
| **`aslr_off`** | Disables ASLR (Address Space Layout Randomization) for debugging. |

### 🌐 CTF: Web & Network
| Command | Description |
| :--- | :--- |
| **`webup`** | Starts a Python HTTP Server on port 80. |
| **`ftpup`** | Starts an anonymous FTP Server on port 21. |
| **`smbup`** | Starts an SMB Share in the current directory (Impacket). |
| **`mscanz <ip>`** | Fast full-port scan using Masscan (Rate: 1000). |
| **`myip`** | Shows Local IP (Cyan) and Public IP (Green). |
| **`vpn-htb`** | Connects to HackTheBox VPN. |

---

## ⚠️ Troubleshooting

1.  **"Command not found: ls"**
    * **Reason:** You are missing the `~/.ltable.py` script referenced in the config.
    * **Fix:** Either download the script or remove the alias `alias ls='python3 ~/.ltable.py'` in `.zshrc`.

2.  **Images not showing in Neofetch (`c` command)**
    * **Reason:** Your terminal emulator does not support **Sixel** graphics.
    * **Fix:** Use **Konsole**, **WezTerm**, or **Foot**. Standard GNOME Terminal does not support this.

3.  **Clipboard copy (`ccfg`, `sshup`) not working**
    * **Reason:** These commands use OSC 52 escape sequences.
    * **Fix:** You must SSH from a client that supports OSC 52, such as **Windows Terminal** or **Tabby**. Putty/MobaXterm may need extra configuration.

---
*Configuration maintained by Zahard.*
```
