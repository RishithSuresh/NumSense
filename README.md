# NumSense - Advanced Number Analysis

A modern, interactive web application for comprehensive mathematical number analysis with powerful features and beautiful UI.

## ✨ Features Overview

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

### 📊 Advanced Features

#### 🧮 Enhanced Number Statistics (14 Statistics)
Comprehensive statistical analysis including:
- **Basic Stats**: Digit sum, product, count, unique digits, max/min digits
- **Mathematical**: Even/odd classification, digit average, divisor count
- **Number Systems**: Binary, octal, hexadecimal representations
- **Advanced**: Digit range, digit variance for deeper insights

#### 🌟 Sequence Generator & Analyzer (NEW!)
Generate and analyze mathematical sequences:
- **Fibonacci Sequence** - Classic recursive sequence
- **Prime Numbers** - Generate prime number sequences
- **Perfect Squares & Cubes** - Geometric number patterns
- **Triangular Numbers** - Triangular dot patterns
- **Factorial Sequence** - Factorial progression
- **Lucas Numbers** - Fibonacci-like sequence
- **Catalan Numbers** - Combinatorial sequence
- **Sequence Analysis** - Sum, average, growth rate, and pattern analysis

#### 🎯 Core Features
- **Check All Properties** - Analyze all 20 properties simultaneously
- **Property Visualization** - Interactive charts showing property distribution
- **Recent History** - Track your recent number checks with timestamps
- **Dark/Light Mode** - Beautiful theme switching with persistence
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

## 🚀 Usage Instructions

### Basic Number Analysis
1. **Enter a Number** - Type any positive integer in the input field
2. **Select Property** - Choose which mathematical property to check
3. **Check Number** - Click "Check Number" for individual analysis
4. **Check All Properties** - Click "Check All Properties" for comprehensive analysis

### Advanced Features
5. **Generate Statistics** - Enter a number in the Statistics section for 14 detailed metrics
6. **Create Sequences** - Select sequence type, set limit, and generate mathematical sequences
7. **Visualize Patterns** - Set number ranges and create interactive charts
8. **View History** - Check recent analyses in the History section

### Tips for Best Experience
- Use the **Random Number Generator** (dice icon) to discover interesting numbers
- Try the **Dark Mode** toggle for comfortable viewing
- **Sequence Generator** works best with limits between 10-50 for readability
- **Property Visualization** is most effective with ranges like 1-100 or 1-1000

## 🛠️ Technical Details

### Architecture
- **Pure Client-Side** - No server required, runs entirely in the browser
- **Single HTML File** - Everything embedded for maximum portability
- **Modern JavaScript** - ES6+ features with optimized algorithms
- **Responsive Design** - Adaptive layout for all screen sizes

### Technologies Used
- **Bootstrap 5** - Modern, accessible UI framework
- **Chart.js** - Interactive data visualization and charts
- **Font Awesome 6** - Comprehensive icon library
- **Animate.css** - Smooth CSS animations and transitions
- **Google Fonts (Inter)** - Professional typography
- **Canvas Confetti** - Celebration animations for positive results

### Performance Features
- **Optimized Algorithms** - Efficient mathematical computations
- **Lazy Loading** - Features load only when needed
- **Local Storage** - Theme preferences persist across sessions
- **Smooth Animations** - Hardware-accelerated CSS transitions

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

## 🎨 UI/UX Features

### Modern Design Elements
- **Glass Morphism** - Translucent cards with backdrop blur effects
- **Gradient Backgrounds** - Beautiful color transitions
- **Hover Animations** - Interactive button and card effects
- **Loading States** - Smooth loading indicators for better UX
- **Responsive Grid** - Adaptive layouts for all screen sizes

### Accessibility
- **High Contrast** - Excellent readability in both light and dark modes
- **Keyboard Navigation** - Full keyboard accessibility support
- **Screen Reader Friendly** - Semantic HTML and ARIA labels
- **Mobile Optimized** - Touch-friendly interface for mobile devices

## 🔧 Development & Customization

### Easy Modification
This is a standalone HTML application. To customize:
1. Edit `index.html` directly - all code is embedded
2. Modify CSS styles in the `<style>` section
3. Update JavaScript functionality in the `<script>` section
4. No build process or dependencies required

### Adding New Features
- **Number Properties**: Add new cases to the switch statements
- **Statistics**: Extend the stats array with new calculations
- **Sequences**: Add new sequence types to the generator
- **Styling**: Modify CSS variables and classes for visual changes

## 📈 Performance Stats

- **File Size**: ~50KB (single HTML file)
- **Load Time**: <1 second on modern browsers
- **Memory Usage**: Minimal JavaScript footprint
- **Compatibility**: Works on 99%+ of modern browsers

## 🌟 What's New in Latest Version

### Version 2.0 Features
- ✅ **4 New Statistics** - Octal, Hexadecimal, Digit Range, Digit Variance
- ✅ **Sequence Generator** - 8 different mathematical sequences with analysis
- ✅ **Enhanced UI** - Improved animations, loading states, and visual polish
- ✅ **Better Performance** - Optimized algorithms and smoother interactions

## 📄 License

**MIT License** - Open source, free to use, modify, and distribute!

---

**Made with ❤️ for mathematics enthusiasts and developers**
