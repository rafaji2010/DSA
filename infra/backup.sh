#!/bin/bash
# infra/backup.sh - Auto-backup with timestamps and logging
# Usage: ./backup.sh [source_dir1] [source_dir2] ...

set -euo pipefail

# ── Configuration ────────────────────────────────────────────────────────
BACKUP_ROOT="$HOME/backups"
LOG_FILE="$BACKUP_ROOT/backup.log"
TIMESTAMP=$(date +"%Y-%m-%d_%H-%M-%S")

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'

# ── Functions ────────────────────────────────────────────────────────────
log() {
    local level=$1
    local message=$2
    local timestamp=$(date +"%Y-%m-%d %H:%M:%S")
    
    case $level in
        INFO)  echo -e "[$timestamp] ${GREEN}INFO${NC} - $message" ;;
        WARN)  echo -e "[$timestamp] ${YELLOW}WARN${NC} - $message" ;;
        ERROR) echo -e "[$timestamp] ${RED}ERROR${NC} - $message" ;;
    esac
    
    echo "[$timestamp] $level - $message" >> "$LOG_FILE"
}

create_dir() {
    if [ ! -d "$1" ]; then
        mkdir -p "$1"
        log "INFO" "Created directory: $1"
    fi
}

backup_dir() {
    local source_dir=$1
    
    if [ ! -d "$source_dir" ]; then
        log "WARN" "Directory not found: $source_dir"
        return 1
    fi
    
    local name=$(basename "$source_dir")
    local dest_dir="$BACKUP_ROOT/${name}_${TIMESTAMP}"
    
    create_dir "$dest_dir"
    cp -r "$source_dir"/* "$dest_dir/" 2>/dev/null || true
    
    local file_count=$(find "$dest_dir" -type f | wc -l | tr -d ' ')
    log "INFO" "Backed up $source_dir → $dest_dir ($file_count files)"
}

# ── Main ─────────────────────────────────────────────────────────────────
create_dir "$BACKUP_ROOT"
log "INFO" "=== Backup session started ==="

# If no arguments, use default directories
if [ $# -eq 0 ]; then
    directories=(
        "$HOME/DSA/core"
        "$HOME/DSA/eval"
    )
else
    directories=("$@")
fi

for dir in "${directories[@]}"; do
    backup_dir "$dir"
done

log "INFO" "=== Backup session completed ==="
echo ""
echo "Backup log: $LOG_FILE"