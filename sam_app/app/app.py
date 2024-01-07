import json
import logging 
import os
import pymysql
import boto3

# Setup logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
formatter = logging.Formatter("%(levelname)s - %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)

def get_document(document_id):
    """
    Retrieve a PDF document.

    :param document_id: The ID of the document to retrieve.
    :return: A dictionary containing the document ID and content.
    """
    try:
        logger.info(f"Retrieving document with ID: {document_id}")
        # Implement logic to retrieve a PDF document from S3 or MySQL
        # For simplicity, this example returns a placeholder response
        result = {"document_id": document_id, "content": "This is a PDF document content."}
        logger.info(f"Document retrieved: {result}")
        return result
    except Exception as e:
        logger.error(f"Error retrieving document: {e}")
        raise

def upload_document(pdf_file):
    """
    Upload a PDF document.

    :param pdf_file: The PDF file to upload.
    :return: A string representing the document ID.
    """
    try:
        logger.info("Uploading document...")
        # Implement logic to upload a PDF document to S3 or MySQL
        # For simplicity, this example returns a placeholder document_id
        document_id = "Your Document has been uploaded into S3 bucket"
        logger.info(f"Document uploaded with ID: {document_id}")
        return document_id
    except Exception as e:
        logger.error(f"Error uploading document: {e}")
        raise

def check_connection():
    """
    Check MySQL database connection.

    Raises:
        pymysql.Error: If there is an error connecting to the database.
    """
    try:
        # Using lazy % formatting in logging functions
        logger.info("The cluster name is %s", os.environ['MYSQL_HOST'])
        connection = pymysql.connect(
            host=os.environ["MYSQL_HOST"],
            port=int(os.environ["MYSQL_PORT"]),  # Make sure to convert port to an integer
            user=os.environ["MYSQL_USER"],
            password=os.environ["MYSQL_PASSWORD"]
        )
        if connection.open:
            logger.info("Connection IS OK")
            return "Connection IS OK"
    except pymysql.Error as e:
        logger.error("Error connecting to the database: %s", e)
        raise
    

def lambda_handler(event, context):
    """
    Lambda function handler.

    :param event: The Lambda event.
    :param context: The Lambda context.
    :return: A dictionary containing the HTTP response.
    """
    try:
        logger.info(f"Received Lambda event: {event}")
        method = event["httpMethod"]
        check_db_con=check_connection()
        s3 = boto3.client("s3")
        response = s3.list_buckets()
        bucket_names = [bucket['Name'] for bucket in response['Buckets']]          
        if method == "GET":
            document_id = event["pathParameters"]["id"]
            logger.info(f"Handling GET request for document ID: {document_id}")
            result = str(check_db_con) + "-" + str(bucket_names) + "-" + str(get_document(document_id))
            return {"statusCode": 200, "body": json.dumps(result)}
        elif method == "POST":
            # Assuming the PDF file is passed in the request body
            pdf_file = event["body"]
            logger.info("Handling POST request to upload document...")
            document_id = check_db_con + "-" + upload_document(pdf_file)
            return {"statusCode": 201, "body": json.dumps({"document_id": document_id})}
        else:
            logger.warning("Invalid HTTP method provided.")
            return {"statusCode": 400, "body": json.dumps({"error": "Invalid HTTP method"})}
    except Exception as e:
        logger.error(f"Error in Lambda function: {e}")
        return {"statusCode": 500, "body": json.dumps({"error": "Internal Server Error"})}
