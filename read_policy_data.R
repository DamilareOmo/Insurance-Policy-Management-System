# =============================================================
# read_policy_data.R
#
# Reads the three CSV files exported by the Insurance Policy
# Management System and provides basic exploration of each.
#
# Usage:
#   1. Run main.py first to generate the CSV files.
#   2. Place this script in the same folder as the CSVs, OR
#      update the file paths in the section below.
#   3. Run in RStudio or from the terminal:  Rscript read_policy_data.R
# =============================================================


# ---------------------------------------------------------
# 1. LOCATE THE CSV FILES
#    The CSVs are named with a timestamp, e.g.:
#      policyholders_20260623_153000.csv
#    This block finds the most recently generated file for
#    each type automatically, so you don't have to rename them.
# ---------------------------------------------------------

get_latest_csv <- function(prefix, folder = ".") {
  matches <- list.files(
    path    = folder,
    pattern = paste0("^", prefix, "_\\d{8}_\\d{6}\\.csv$"),
    full.names = TRUE
  )
  if (length(matches) == 0) {
    stop(paste("No CSV file found with prefix:", prefix))
  }
  # Return the most recently modified file
  matches[which.max(file.mtime(matches))]
}

policyholders_file <- get_latest_csv("policyholders")
products_file      <- get_latest_csv("products")
payments_file      <- get_latest_csv("payments")

cat("Files found:\n")
cat(" ", policyholders_file, "\n")
cat(" ", products_file, "\n")
cat(" ", payments_file, "\n\n")


# ---------------------------------------------------------
# 2. READ THE CSV FILES
# ---------------------------------------------------------

policyholders <- read.csv(policyholders_file, stringsAsFactors = FALSE)
products      <- read.csv(products_file,      stringsAsFactors = FALSE)
payments      <- read.csv(payments_file,      stringsAsFactors = FALSE)

# Convert date columns from character to Date type
policyholders$Registered.On <- as.Date(policyholders$Registered.On)
payments$Date.Paid          <- as.Date(payments$Date.Paid, optional = TRUE)


# ---------------------------------------------------------
# 3. EXPLORE POLICYHOLDERS
# ---------------------------------------------------------

cat("=== POLICYHOLDERS ===\n")
print(policyholders)

cat("\nColumn names:\n")
print(colnames(policyholders))

cat("\nStructure:\n")
str(policyholders)

cat("\nStatus summary:\n")
print(table(policyholders$Status))


# ---------------------------------------------------------
# 4. EXPLORE PRODUCTS
# ---------------------------------------------------------

cat("\n=== PRODUCTS ===\n")
print(products)

cat("\nColumn names:\n")
print(colnames(products))

cat("\nStructure:\n")
str(products)

cat("\nStatus summary:\n")
print(table(products$Status))

cat("\nPremium range:\n")
cat("  Min: $", min(products$Premium....month.), "\n")
cat("  Max: $", max(products$Premium....month.), "\n")


# ---------------------------------------------------------
# 5. EXPLORE PAYMENTS
# ---------------------------------------------------------

cat("\n=== PAYMENTS ===\n")
print(payments)

cat("\nColumn names:\n")
print(colnames(payments))

cat("\nStructure:\n")
str(payments)

cat("\nPayment status summary:\n")
print(table(payments$Status))

cat("\nTotal collected per policyholder:\n")
totals <- aggregate(
  Amount.Paid.... ~ Policyholder.Name,
  data = payments,
  FUN  = sum
)
colnames(totals) <- c("Policyholder", "Total Paid ($)")
print(totals)

cat("\nGrand total collected: $",
    sum(payments$Amount.Paid...., na.rm = TRUE), "\n")
