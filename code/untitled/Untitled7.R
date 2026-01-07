# Load required libraries
library(ggplot2)
library(ggforce)

# Data for boxes
boxes <- data.frame(
  label = c("Input Signals", "Complexity Metrics", "MHDI Output"),
  x = c(1, 2, 3),
  y = c(3, 3, 3),
  fill = c("lightblue", "lightgreen", "salmon")
)

# Arrows
arrows <- data.frame(
  x = c(1.2, 2.2),
  xend = c(1.8, 2.8),
  y = c(3, 3),
  yend = c(3, 3)
)

# Subtexts
subtexts <- data.frame(
  x = rep(c(1, 2, 3), each = 3),
  y = rep(c(2.75, 2.65, 2.55), times = 3),
  text = c(
    "• Heart Rate (HR)", "• Respiration", "• Temperature",
    "• Entropy (SampEn)", "• Fractality", "• Autocorrelation",
    "• Continuous Score", "• Classifier", "• Risk Strata"
  )
)

# Validation text
validation <- data.frame(
  x = 2, y = c(2.2, 2.1, 2.0),
  text = c("Validation:", "• Holter (high-res)", "• All of Us (5-min HR)")
)

# Applications
applications <- data.frame(
  x = 2, y = c(1.2, 1.1, 1.0),
  text = c("Applications of MHDI:",
           "• Quantify physiological adaptability",
           "• Stratify health states")
)

# Plot
ggplot() +
  # Boxes
  geom_rect(data = boxes, aes(xmin = x - 0.4, xmax = x + 0.4, ymin = 2.2, ymax = 3.1, fill = fill),
            color = "black", alpha = 0.6) +
  geom_text(data = boxes, aes(x = x, y = 3.05, label = label), fontface = "bold", size = 4.5) +
  
  # Arrows
  geom_segment(data = arrows, aes(x = x, xend = xend, y = y, yend = yend),
               arrow = arrow(length = unit(0.25, "cm")), size = 1) +
  
  # Subtext under boxes
  geom_text(data = subtexts, aes(x = x, y = y, label = text), size = 3.5, hjust = 0.5) +
  
  # Validation text
  geom_text(data = validation, aes(x = x, y = y, label = text), fontface = "italic", size = 3.5) +
  
  # Applications
  geom_text(data = applications, aes(x = x, y = y, label = text), fontface = "bold", size = 3.5, hjust = 0.5) +
  
  # Title
  annotate("text", x = 2, y = 3.4, label = "Multiscale Health Dynamics Index (MHDI): Conceptual Framework",
           fontface = "bold", size = 5) +
  
  scale_fill_identity() +
  xlim(0.5, 3.5) +
  ylim(0.8, 3.5) +
  theme_void()





library(statcomp)
