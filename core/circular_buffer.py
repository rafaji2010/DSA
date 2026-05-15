"""
core/circular_buffer.py
Fixed-size circular buffer (ring buffer) that overwrites oldest data when full.
"""

from typing import TypeVar, Generic, Optional

T = TypeVar("T")


class CircularBuffer(Generic[T]):
    """
    Fixed-size circular buffer.
    
    When full, writing new data overwrites the oldest data (FIFO behavior).
    Useful for:
    - Audio/video streaming (latest frame overwrites oldest)
    - Log management (keep last N messages)
    - Real-time data processing
    """
    
    def __init__(self, capacity: int):
        """
        Initialize circular buffer with fixed capacity.
        
        Raises:
            ValueError: If capacity <= 0
        """
        if capacity <= 0:
            raise ValueError(f"Capacity must be positive, got {capacity}")
        
        self._capacity = capacity
        self._buffer: list[Optional[T]] = [None] * capacity
        self._read_pos = 0
        self._write_pos = 0
        self._size = 0
    
    def write(self, item: T) -> None:
        """
        Write an item to the buffer.
        If buffer is full, overwrites the oldest item.
        
        Time: O(1)
        """
        # Overwrite the write position
        self._buffer[self._write_pos] = item
        
        # Move write position forward (wrap around)
        self._write_pos = (self._write_pos + 1) % self._capacity
        
        # If buffer was full, read position advances (we overwrote oldest)
        if self._size == self._capacity:
            self._read_pos = (self._read_pos + 1) % self._capacity
        else:
            self._size += 1
    
    def read(self) -> T:
        """
        Read and remove the oldest item from the buffer.
        
        Returns:
            The oldest item
        
        Raises:
            IndexError: If buffer is empty
        """
        if self.is_empty():
            raise IndexError("Cannot read from empty buffer")
        
        # Get value at read position
        value = self._buffer[self._read_pos]
        if value is None:
            raise IndexError("Buffer corruption detected")
        
        # Clear the slot (optional, helps debugging)
        self._buffer[self._read_pos] = None
        
        # Move read position forward
        self._read_pos = (self._read_pos + 1) % self._capacity
        self._size -= 1
        
        return value
    
    def peek(self) -> T:
        """
        View the oldest item without removing it.
        
        Returns:
            The oldest item
        
        Raises:
            IndexError: If buffer is empty
        """
        if self.is_empty():
            raise IndexError("Cannot peek at empty buffer")
        
        value = self._buffer[self._read_pos]
        if value is None:
            raise IndexError("Buffer corruption detected")
        
        return value
    
    def is_empty(self) -> bool:
        """Return True if buffer has no items."""
        return self._size == 0
    
    def is_full(self) -> bool:
        """Return True if buffer has reached capacity."""
        return self._size == self._capacity
    
    def size(self) -> int:
        """Return number of items currently in buffer."""
        return self._size
    
    def capacity(self) -> int:
        """Return maximum capacity of buffer."""
        return self._capacity
    
    def clear(self) -> None:
        """Remove all items from buffer."""
        self._buffer = [None] * self._capacity
        self._read_pos = 0
        self._write_pos = 0
        self._size = 0
    
    def __len__(self) -> int:
        """Allow len(buffer) syntax."""
        return self.size()
    
    def __repr__(self) -> str:
        """String representation for debugging."""
        if self.is_empty():
            return "CircularBuffer(empty)"
        
        # Show items in order (oldest to newest)
        items = []
        pos = self._read_pos
        for _ in range(self._size):
            if self._buffer[pos] is not None:
                items.append(str(self._buffer[pos]))
            pos = (pos + 1) % self._capacity
        
        return f"CircularBuffer(cap={self._capacity}, size={self._size}, items=[{', '.join(items)}])"


if __name__ == "__main__":
    print("=" * 60)
    print("CIRCULAR BUFFER (RING BUFFER)")
    print("=" * 60)
    
    # Create buffer of size 4
    buffer = CircularBuffer[int](4)
    print(f"Created buffer: {buffer}")
    print(f"Capacity: {buffer.capacity()}")
    print(f"Empty: {buffer.is_empty()}")
    
    print("\n--- Writing values 1, 2, 3, 4 ---")
    for i in range(1, 5):
        buffer.write(i)
        print(f"  write({i}) → buffer: {buffer}")
    
    print(f"\nBuffer full: {buffer.is_full()}")
    print(f"Size: {buffer.size()}")
    
    print("\n--- Reading (FIFO order) ---")
    for i in range(4):
        value = buffer.read()
        print(f"  read() → {value}, buffer: {buffer}")
    
    print("\n--- Buffer empty now ---")
    print(f"Empty: {buffer.is_empty()}")
    
    print("\n--- Writing to full buffer (overwrites oldest) ---")
    # Fill buffer
    for i in range(1, 5):
        buffer.write(i * 10)
    print(f"Buffer after writes 10,20,30,40: {buffer}")
    
    # Write one more - should overwrite 10
    buffer.write(50)
    print(f"Buffer after write(50): {buffer}")
    print("Notice: 10 was overwritten (oldest), 50 is now newest")
    
    # Read all
    print("\n--- Reading all ---")
    while not buffer.is_empty():
        print(f"  read() → {buffer.read()}")
    
    print("\n--- Edge Cases ---")
    buffer2 = CircularBuffer[str](3)
    
    # Test overwrite
    for letter in ['A', 'B', 'C', 'D', 'E']:
        buffer2.write(letter)
        print(f"write('{letter}') → {buffer2}")
    
    # Test read from empty
    buffer3 = CircularBuffer[int](2)
    try:
        buffer3.read()
    except IndexError as e:
        print(f"\n✅ Caught expected error: {e}")
    
    # Test invalid capacity
    try:
        buffer4 = CircularBuffer[int](0)
    except ValueError as e:
        print(f"✅ Caught expected error: {e}")
    
    print("\n✅ Circular Buffer implementation complete!")