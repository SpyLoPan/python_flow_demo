import pandas as pd
from etl.common.logger import get_logger


def run():
    logger = get_logger("pipeline.step1_aggregate")
    logger.info("Starting step1_aggregate pipeline")

    # Dummy dataset (sales lines)
    df = pd.DataFrame(
        {
            "customer": ["A", "A", "B", "B", "C"],
            "product": ["p1", "p2", "p1", "p3", "p2"],
            "qty": [1, 2, 1, 5, 3],
            "amount": [10.0, 40.0, 10.0, 100.0, 60.0],
        }
    )

    logger.info(f"Loaded {len(df)} raw records")

    # Aggregate per customer
    agg = (
        df.groupby("customer", as_index=False)
        .agg(
            total_qty=("qty", "sum"),
            total_amount=("amount", "sum"),
        )
        .sort_values("customer")
    )

    logger.info(f"Produced {len(agg)} aggregated records")

    print("\nAGGREGATED RESULT")
    print(agg)

    logger.info("Finished step1_aggregate pipeline")
