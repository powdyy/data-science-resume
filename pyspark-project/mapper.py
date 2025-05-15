
from pyspark.sql import DataFrame
from pyspark.sql.functions import col

def map_products_to_categories(
    products_df: DataFrame,
    categories_df: DataFrame,
    product_category_df: DataFrame
) -> DataFrame:
    """
    Возвращает DataFrame с парами "Имя продукта – Имя категории" и включает продукты без категорий.
    
    :param products_df: DataFrame с колонками (product_id, product_name)
    :param categories_df: DataFrame с колонками (category_id, category_name)
    :param product_category_df: DataFrame с колонками (product_id, category_id)
    :return: DataFrame с колонками (product_name, category_name)
    """
    joined_df = products_df.join(
        product_category_df,
        on="product_id",
        how="left"
    ).join(
        categories_df,
        on="category_id",
        how="left"
    ).select(
        col("product_name"),
        col("category_name")
    )
    return joined_df
