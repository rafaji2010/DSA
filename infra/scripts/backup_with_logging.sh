#!/bin/bash
# ============================================
# Advanced Backup Script with Logging
# ============================================

set -euo pipefail  # Exit on error, undefined var, pipe failure

# Configuration
BACKUP_ROOT="$HOME/backups"
LOG_FILE="$BACKUP_ROOT/backup.log"
TIMESTAMP=$(date +"%Y-%m-%d_%H-%M-%S")

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Logging function
log() {
    local level=$1
    local message=$2
    local timestamp=$(date +"%Y-%m-%d %H:%M:%S")
    
    case $level in
        INFO)  echo -e "[$timestamp] ${GREEN}INFO${NC} - $message" ;;
        WARN)  echo -e "[$timestamp] ${YELLOW}WARN${NC} - $message" ;;
        ERROR) echo -e "[$timestamp] ${RED}ERROR${NC} - $message" ;;
        *)     echo -e "[$timestamp] - $message" ;;
    esac
    
    echo "[$timestamp] $level - $message" >> "$LOG_FILE"
}

# Create directory with error handling
create_dir() {
    local dir=$1
    if [ ! -d "$dir" ]; then
        mkdir -p "$dir"
        log "INFO" "Created directory: $dir"
    fi
}

# Backup single directory
backup_dir() {
    local source_dir=$1
    local dest_base=$2
    
    if [ ! -d "$source_dir" ]; then
        log "WARN" "Directory not found: $source_dir"
        return 1
    fi
    
    local name=$(basename "$source_dir")
    local dest_dir="$dest_base/${name}_${TIMESTAMP}"
    
    create_dir "$dest_dir"
    cp -r "$source_dir"/* "$dest_dir/" 2>/dev/null || true
    
    local file_count=$(find "$dest_dir" -type f | wc -l)
    log "INFO" "Backed up $source_dir → $dest_dir ($file_count files)"
}

# Cleanup old backups (keep last 5)
cleanup_old() {
    local backup_dir=$1
    local keep=${2:-5}
    
    if [ ! -d "$backup_dir" ]; then
        return 0
    fi
    
    local count=0
    while IFS= read -r dir; do
        ((count++))
        if [ $count -gt $keep ]; then
            rm -rf "$dir"
            log "INFO" "Removed old backup: $dir"
        fi
    done < <(ls -dt "$backup_dir"/*/ 2>/dev/null || true)
}

# Main function
main() {
    log "INFO" "=== Backup session started ==="
    
    # Create backup root
    create_dir "$BACKUP_ROOT"
    
    # Directories to backup
    directories=(
        "$HOME/linux_practice"
        "/mnt/d/DSA/core"
    )
    
    # Backup each directory
    for dir in "${directories[@]}"; do
        backup_dir "$dir" "$BACKUP_ROOT"
    done
    
    # Cleanup old backups (keep last 5)
    cleanup_old "$BACKUP_ROOT" 5
    
    log "INFO" "=== Backup session completed ==="
    echo ""
    echo "Backup log: $LOG_FILE"
}

# Run main function
main "$@"
