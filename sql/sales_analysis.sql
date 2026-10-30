-- ==========================================
-- 1. BUSINESS OVERVIEW
-- ==========================================

SELECT
    COUNT(*) AS total_transactions,
    SUM(sales) AS total_sales,
    SUM(profit) AS total_profit,
    ROUND(
        (
            SUM(profit)::NUMERIC
            / NULLIF(SUM(sales)::NUMERIC, 0)
        ) * 100,
        2
    ) AS overall_profit_margin
FROM clean_transactions;


-- ==========================================
-- 2. MONTHLY SALES PERFORMANCE
-- ==========================================

SELECT
    DATE_TRUNC(
        'month',
        order_date::DATE
    ) AS sales_month,

    COUNT(*) AS total_transactions,

    ROUND(SUM(sales)::NUMERIC, 2) AS total_sales,

    ROUND(SUM(profit)::NUMERIC, 2) AS total_profit

FROM clean_transactions
GROUP BY DATE_TRUNC('month', order_date::DATE)
ORDER BY sales_month ASC;


-- ==========================================
-- 3. SALES PERFORMANCE BY CATEGORY
-- ==========================================

SELECT
    category,
    COUNT(*) AS total_transactions,
    ROUND(SUM(sales)::NUMERIC, 2) AS total_sales,
    ROUND(SUM(profit)::NUMERIC, 2) AS total_profit,
    ROUND(
        (
            SUM(profit)::NUMERIC
            / NULLIF(SUM(sales)::NUMERIC, 0)
        ) * 100,
        2
    ) AS profit_margin_pct

FROM clean_transactions
GROUP BY category
ORDER BY total_sales DESC;

-- ==========================================
-- 4. TOP 10 PRODUCTS BY SALES
-- ==========================================

SELECT
    product_name,
    category,
    sub_category,
    SUM(quantity) AS total_quantity_sold,
    ROUND(SUM(sales)::NUMERIC, 2) AS total_sales,
    ROUND(SUM(profit)::NUMERIC, 2) AS total_profit

FROM clean_transactions

GROUP BY
    product_name,
    category,
    sub_category

ORDER BY total_sales DESC

LIMIT 10;

-- ==========================================
-- 5. SALES PERFORMANCE BY REGION
-- ==========================================

SELECT
    region,
    COUNT(*) AS total_transactions,
    COUNT(DISTINCT order_id) AS unique_orders,
    ROUND(SUM(sales)::NUMERIC, 2) AS total_sales,
    ROUND(SUM(profit)::NUMERIC, 2) AS total_profit,
    ROUND(
        (
            SUM(profit)::NUMERIC
            / NULLIF(SUM(sales)::NUMERIC, 0)
        ) * 100,
        2
    ) AS profit_margin_pct

FROM clean_transactions
GROUP BY region
ORDER BY total_sales DESC;

-- ==========================================
-- 6. LOSS-MAKING SUB-CATEGORIES
-- ==========================================

SELECT
    category,
    sub_category,
    COUNT(*) AS total_transactions,
    ROUND(SUM(sales)::NUMERIC, 2) AS total_sales,
    ROUND(SUM(profit)::NUMERIC, 2) AS total_profit

FROM clean_transactions

GROUP BY
    category,
    sub_category

HAVING SUM(profit) < 0
ORDER BY total_profit ASC;