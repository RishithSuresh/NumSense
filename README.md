# NumSense - Advanced Number Analysis

A modern, interactive web application for analyzing mathematical properties of numbers.

## Features

### 🔢 Number Property Analysis
Analyze numbers for **20 different mathematical properties**:

**Basic Properties:**
- **Palindrome** - Reads the same backward as forward
- **Prime** - Only divisible by 1 and itself
- **Armstrong** - Sum of digits raised to power of digit count
- **Perfect** - Sum of proper divisors equals the number
- **Fibonacci** - Part of the Fibonacci sequence

**Advanced Properties:**
- **Happy Number** - Eventually reaches 1 through sum of squares of digits
- **Magic Number** - Becomes 1 when digits are summed repeatedly
- **Triangular Number** - Can form triangular patterns
- **Perfect Square** - Square of an integer
- **Perfect Cube** - Cube of an integer
- **Harshad Number** - Divisible by sum of its digits
- **Abundant Number** - Sum of proper divisors > number
- **Deficient Number** - Sum of proper divisors < number
- **Automorphic Number** - Appears at end of its square
- **Kaprekar Number** - Square can be split into parts that sum to original
- **Neon Number** - Equals sum of digits of its square
- **Spy Number** - Sum equals product of digits
- **Duck Number** - Contains 0 but doesn't start with 0
- **Buzz Number** - Divisible by 7 or contains digit 7
- **Pronic Number** - Product of consecutive integers

### 📊 Additional Features
- **Number Statistics** - Comprehensive analysis including digit sum, product, binary representation, etc.
- **Check All Properties** - Analyze all 20 properties at once
- **Property Visualization** - Chart showing property distribution in number ranges
- **Recent History** - Track your recent number checks
- **Dark/Light Mode** - Toggle between themes
- **Random Number Generator** - Generate random numbers for testing

## How to Use

### Option 1: Direct Browser Access
1. Simply open `index.html` in any modern web browser
2. No server or installation required!

### Option 2: Local Server (Optional)
If you prefer to run it on a local server:
```bash
# Using Python's built-in server
python -m http.server 8000

# Using Node.js http-server
npx http-server

# Then open http://localhost:8000
```

## Usage Instructions

1. **Enter a Number** - Type any positive integer in the input field
2. **Select Property** - Choose which mathematical property to check
3. **Check Number** - Click "Check Number" for individual analysis
4. **Check All Properties** - Click "Check All Properties" for comprehensive analysis
5. **Generate Statistics** - Use the Number Statistics feature for detailed analysis
6. **Visualize Range** - Create charts showing property distribution across number ranges

## Technical Details

- **Pure Client-Side** - No server required, runs entirely in the browser
- **Modern JavaScript** - Uses ES6+ features for optimal performance
- **Responsive Design** - Works on desktop, tablet, and mobile devices
- **Bootstrap 5** - Modern, accessible UI components
- **Chart.js** - Interactive data visualization
- **Font Awesome** - Beautiful icons throughout
- **Animate.css** - Smooth animations and transitions

## Browser Compatibility

- Chrome 60+
- Firefox 55+
- Safari 12+
- Edge 79+

## File Structure

```
NumSense/
├── index.html          # Main application file
└── README.md          # This file
```

## Contributing

This is a standalone HTML application. To modify:
1. Edit `index.html` directly
2. All JavaScript is embedded in the HTML file
3. All CSS is embedded in the HTML file
4. No build process required

## License

Open source - feel free to use, modify, and distribute!
