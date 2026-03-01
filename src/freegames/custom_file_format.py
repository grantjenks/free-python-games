import struct
import pygame
import io
import sys

class DaychIO:
    """
    A utility class for the .daych custom image format.
    Designed for high-performance Pygame surface manipulation.
    """
    HEADER_FORMAT = "!5sBHHB"  # Sig(5), Ver(1), W(2), H(2), BPP(1)
    HEADER_SIZE = struct.calcsize(HEADER_FORMAT)
    SIGNATURE = b"DAYCH"

    @staticmethod
    def load_surface(source):
        """
        Decodes .daych data from a file path or BytesIO buffer into a pygame.Surface.
        """
        is_path = isinstance(source, (str, bytes))
        f = open(source, 'rb') if is_path else source

        try:
            header_bytes = f.read(DaychIO.HEADER_SIZE)
            if len(header_bytes) < DaychIO.HEADER_SIZE:
                raise ValueError("Invalid Header: Data truncated.")

            sig, ver, w, h, bpp = struct.unpack(DaychIO.HEADER_FORMAT, header_bytes)

            if sig != DaychIO.SIGNATURE:
                raise ValueError(f"Signature mismatch: Expected {DaychIO.SIGNATURE}, got {sig}")

            pixel_data = f.read()
            # Directly convert raw bytes to Surface (Efficient RAM usage)
            return pygame.image.frombytes(pixel_data, (w, h), "RGB")
        
        finally:
            if is_path:
                f.close()

    @staticmethod
    def save_surface(surface, filename):
        """
        Encodes a pygame.Surface into a .daych file on disk.
        """
        width, height = surface.get_size()
        # Extract raw RGB data from the surface
        pixel_data = pygame.image.tostring(surface, "RGB")
        
        header = struct.pack(DaychIO.HEADER_FORMAT, DaychIO.SIGNATURE, 1, width, height, 24)
        
        with open(filename, "wb") as f:
            f.write(header + pixel_data)

    @staticmethod
    def to_buffer(surface):
        """
        Encodes a pygame.Surface into a BytesIO buffer (RAM only).
        """
        width, height = surface.get_size()
        pixel_data = pygame.image.tostring(surface, "RGB")
        
        buffer = io.BytesIO()
        header = struct.pack(DaychIO.HEADER_FORMAT, DaychIO.SIGNATURE, 1, width, height, 24)
        buffer.write(header + pixel_data)
        buffer.seek(0)
        return buffer

# --- Demo/Test Logic ---
def run_demo():
    pygame.init()
    screen = pygame.display.set_mode((400, 400))
    pygame.display.set_caption("DAYCH Format Engine")

    # 1. Create a surface manually (Simulating an Aseprite export or game icon)
    test_surf = pygame.Surface((32, 32))
    test_surf.fill((255, 100, 0)) # Orange pixel art base
    pygame.draw.rect(test_surf, (255, 255, 255), (8, 8, 16, 16)) # White center

    # 2. Save to RAM and reload (The "No SSD wear" method)
    mem_file = DaychIO.to_buffer(test_surf)
    loaded_surf = DaychIO.load_surface(mem_file)

    # 3. Scale it up so we can see the pixels (Aseprite style!)
    display_surf = pygame.transform.scale(loaded_surf, (128, 128))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill((20, 20, 25)) # Professional dark theme
        screen.blit(display_surf, (136, 136))
        pygame.display.flip()

if __name__ == "__main__":
    run_demo()