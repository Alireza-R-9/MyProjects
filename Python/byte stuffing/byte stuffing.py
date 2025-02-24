import random


def generate_random_bits(length, frame_size):
    bits = ''.join([random.choice('01') for _ in range(length)])
    return [bits[i:i+frame_size] for i in range(0, length, frame_size)]


def encode(frames):
    encoded_frames = []
    for frame in frames:
        frame = frame.replace('101', '100101')
        frame = frame.replace('100', '100100')
        frame = frame.replace('1001001', '1001001001001')
        frame = frame.replace('100100', '1001001001001')
        frame = '101' + frame + '101'
        encoded_frames.append(frame)
    return encoded_frames


def decode(frames):
    decoded_frames = []
    for frame in frames:
        frame = frame[3:-3]
        frame = frame.replace('1001001001001', '100100')
        frame = frame.replace('1001001001001', '1001001')
        frame = frame.replace('100100', '100')
        frame = frame.replace('100101', '101')
        decoded_frames.append(frame)
    return decoded_frames


def compare_bits(initial_frames, decoded_frames):
    for initial_frame, decoded_frame in zip(initial_frames, decoded_frames):
        if initial_frame != decoded_frame:
            return False
    return True


def main():
    frame_size = 100
    total_bits = 1000
    initial_frames = generate_random_bits(total_bits, frame_size)
    print("Initial frames ({} frames):".format(len(initial_frames)), initial_frames)

    encoded_frames = encode(initial_frames)
    print("Encoded frames ({} frames):".format(len(encoded_frames)), encoded_frames)

    decoded_frames = decode(encoded_frames)
    print("Decoded frames ({} frames):".format(len(decoded_frames)), decoded_frames)

    result = compare_bits(initial_frames, decoded_frames)
    if result:
        print("Bits are identical: True")
    else:
        print("Bits are identical: False")


if __name__ == "__main__":
    main()
