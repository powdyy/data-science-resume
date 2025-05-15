
from pyspark.sql import SparkSession

if __name__ == "__main__":
    spark = SparkSession.builder.appName("ProductCategoryMapper").getOrCreate()

    products_data = [(1, "Laptop"), (2, "Smartphone"), (3, "Tablet")]
    categories_data = [(10, "Electronics"), (11, "Mobile Devices")]
    product_category_data = [(1, 10), (2, 10), (2, 11)]

    products_df = spark.createDataFrame(products_data, ["product_id", "product_name"])
    categories_df = spark.createDataFrame(categories_data, ["category_id", "category_name"])
    product_category_df = spark.createDataFrame(product_category_data, ["product_id", "category_id"])

    from pyspark_product_category_mapper.mapper import map_products_to_categories
    result_df = map_products_to_categories(products_df, categories_df, product_category_df)

    result_df.show()
    spark.stop()
