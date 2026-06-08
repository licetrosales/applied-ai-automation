# n8n Installation (macOS)

## Goal

Install and run a local n8n Community Edition instance on macOS for learning workflow automation, AI integrations, and local LLM experimentation.

## Tools Used

* macOS
* Homebrew
* nvm (Node Version Manager)
* Node.js 22 LTS
* npm
* n8n Community Edition

## Prerequisites

Verify Homebrew is installed:

```bash
brew --version
```

Expected output:

```text
Homebrew x.x.x
```

## Installation

### Install nvm

Install Node Version Manager using Homebrew:

```bash
brew install nvm
```

Create the nvm working directory:

```bash
mkdir ~/.nvm
```

Add the following configuration to `~/.zshrc`:

```bash
export NVM_DIR="$HOME/.nvm"
[ -s "/opt/homebrew/opt/nvm/nvm.sh" ] && \. "/opt/homebrew/opt/nvm/nvm.sh"
[ -s "/opt/homebrew/opt/nvm/etc/bash_completion.d/nvm" ] && \. "/opt/homebrew/opt/nvm/etc/bash_completion.d/nvm"
```

Reload the shell:

```bash
source ~/.zshrc
```

Verify installation:

```bash
nvm --version
```

### Install Node.js 22 LTS

Install the current n8n-supported LTS version:

```bash
nvm install 22
```

Activate the version:

```bash
nvm use 22
```

Verify:

```bash
node -v
npm -v
```

Example output:

```text
v22.22.3
10.9.8
```

### Install n8n

Install n8n globally:

```bash
npm install -g n8n
```

Verify installation:

```bash
n8n --version
```

Example output:

```text
2.23.4
```

## Verification

Confirm the active Node.js version:

```bash
nvm ls
```

Expected result:

```text
-> v22.x.x
default -> 22
```

## First Launch

Start n8n:

```bash
n8n
```

Open:

```text
http://localhost:5678
```

Create the owner account and complete the initial setup wizard.

## Key Learnings

- n8n requires a supported Node.js version.
- nvm allows multiple Node.js versions on the same machine.
- npm is installed together with Node.js.
- Local installation is ideal for experimentation and learning.
- The Community Edition provides sufficient functionality for personal projects and portfolio development.
