# Image Fetcher Tool 📸

A simple Python script that downloads images from URLs and saves them locally in an organized folder structure.

## Features

✅ **URL Input**: Interactive prompt for image URL  
✅ **Error Handling**: Robust error handling for network and file operations  
✅ **Auto Organization**: Creates dedicated folder for downloaded images  
✅ **Smart Naming**: Extracts filename from URL or generates timestamp-based names  
✅ **Timeout Protection**: 10-second timeout prevents hanging requests

## Requirements

```bash
pip install requests
```

**Standard Libraries Used:**

- `os` - File system operations
- `urllib.parse` - URL parsing
- `datetime` - Timestamp generation

## Installation

1. Clone or download the script
2. Install required dependencies:
   ```bash
   pip install requests
   ```
3. Run the script:
   ```bash
   python image_fetcher.py
   ```

## Usage

1. **Run the script:**

   ```bash
   python answers.py
   ```

2. **Enter image URL when prompted:**

   ```
   Enter the URL of the image you want to fetch: https://example.com/photo.jpg
   ```

3. **Image automatically saved to:**
   ```
   /your-script-directory/Fetched_Images/photo.jpg
   ```

## How It Works

### 1. User Input

```python
url = input("Enter the URL of the image you want to fetch: ").strip()
```

- Prompts user for image URL
- Strips whitespace for clean input

### 2. HTTP Request

```python
response = requests.get(url, timeout=10)
response.raise_for_status()
```

- Fetches image with 10-second timeout
- Raises exception for HTTP errors (404, 500, etc.)

### 3. Directory Creation

```python
script_dir = os.path.dirname(os.path.abspath(__file__))
images_dir = os.path.join(script_dir, "Fetched_Images")
os.makedirs(images_dir, exist_ok=True)
```

- Creates `Fetched_Images` folder in script directory
- Uses `exist_ok=True` to avoid errors if folder exists

### 4. Smart Filename Handling

```python
parsed_url = urlparse(url)
filename = os.path.basename(parsed_url.path)

if not filename or '.' not in filename:
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    filename = f"image_{timestamp}.jpg"
```

- Extracts filename from URL path
- Generates timestamp-based name if no filename found
- Format: `image_YYYYMMDDHHMMSS.jpg`

### 5. File Saving

```python
with open(file_path, "wb") as f:
    f.write(response.content)
```

- Saves image in binary mode (`wb`)
- Handles large files efficiently

## Error Handling

### Network Errors

- **Connection timeout**: 10-second limit prevents hanging
- **HTTP errors**: 404, 500, etc. caught and reported
- **Invalid URLs**: Malformed URLs handled gracefully

### File System Errors

- **Permission issues**: Write permission errors caught
- **Disk space**: Full disk errors handled
- **Invalid paths**: Path creation errors managed

### User Input Errors

- **Empty input**: Exits gracefully if no URL entered
- **Invalid URLs**: Network layer handles malformed URLs

## Example Output

### Successful Download

```
Enter the URL of the image you want to fetch: https://picsum.photos/800/600
Image saved successfully as: /path/to/script/Fetched_Images/600
```

### Generated Filename

```
Enter the URL of the image you want to fetch: https://api.unsplash.com/photo/random
Image saved successfully as: /path/to/script/Fetched_Images/image_20241215143022.jpg
```

### Error Handling

```
Enter the URL of the image you want to fetch: https://invalid-url.com/missing.jpg
Error fetching the image: 404 Client Error: Not Found for url: https://invalid-url.com/missing.jpg
```

## File Structure

```
your-project/
├── image_fetcher.py          # Main script
└── Fetched_Images/           # Auto-created folder
    ├── photo1.jpg
    ├── image_20241215143022.jpg
    └── downloaded_image.png
```

## Supported Image Formats

The script works with any binary file format:

- **Images**: JPG, PNG, GIF, WebP, BMP, SVG
- **Other files**: PDF, ZIP (if served as binary)

Format detection is based on URL path and server response.

## Security Considerations

⚠️ **Important Security Notes:**

- Only download from trusted sources
- Script doesn't validate file content
- Large files will consume disk space
- No virus scanning performed

## Troubleshooting

### Common Issues

**"Module not found: requests"**

```bash
pip install requests
```

**"Permission denied"**

- Check write permissions in script directory
- Run with appropriate user privileges

**"Connection timeout"**

- Check internet connection
- Try increasing timeout value
- Verify URL is accessible

**"No filename detected"**

- Normal behavior for dynamic URLs
- Automatic timestamp naming used
