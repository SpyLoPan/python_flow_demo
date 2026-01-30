import sys
from etl.common.logger import get_logger


def main():
    logger = get_logger("runner")

    if len(sys.argv) < 2:
        logger.error("No pipeline name provided")
        print("Usage: python cli/run_pipeline.py <pipeline_name>")
        sys.exit(1)

    pipeline_name = sys.argv[1].strip()
    logger.info(f"Requested pipeline: {pipeline_name}")

    if pipeline_name == "step1_aggregate":
        from etl.pipelines.step1_aggregate.pipeline import run
    else:
        logger.error(f"Unknown pipeline: {pipeline_name}")
        print(f"Unknown pipeline: {pipeline_name}")
        sys.exit(1)

    logger.info(f"Starting pipeline: {pipeline_name}")
    run()
    logger.info(f"Finished pipeline: {pipeline_name}")


if __name__ == "__main__":
    main()
