"""
Weaviate database schema for CAD AI system.

Collections:
- DesignEmbeddings: Historical part designs with embeddings
- ManufacturingRules: DFM rules encoded as vectors for semantic search
- AuditLog: Governance and compliance audit trail
"""

WEAVIATE_SCHEMA = {
    "classes": [
        {
            "class": "DesignEmbedding",
            "description": "Historical part design with embedding for semantic search",
            "vectorizer": "text2vec-openai",
            "moduleConfig": {
                "text2vec-openai": {
                    "model": "text-embedding-3-small",
                }
            },
            "properties": [
                {
                    "name": "part_id",
                    "dataType": ["string"],
                    "description": "Unique part identifier from ProtoLabs database",
                },
                {
                    "name": "part_name",
                    "dataType": ["string"],
                    "description": "Human-readable part name",
                },
                {
                    "name": "description",
                    "dataType": ["text"],
                    "description": "Part description for semantic search",
                },
                {
                    "name": "process_type",
                    "dataType": ["string"],
                    "description": "Manufacturing process: cnc | molding | sheet_metal | 3d_print",
                },
                {
                    "name": "material",
                    "dataType": ["string"],
                    "description": "Part material (e.g., aluminum 6061, ABS, steel 1018)",
                },
                {
                    "name": "weight_g",
                    "dataType": ["number"],
                    "description": "Part weight in grams",
                },
                {
                    "name": "cost_usd",
                    "dataType": ["number"],
                    "description": "Manufacturing cost estimate",
                },
                {
                    "name": "defect_rate",
                    "dataType": ["number"],
                    "description": "Historical defect rate (0.0 to 1.0)",
                },
                {
                    "name": "rework_rate",
                    "dataType": ["number"],
                    "description": "Rework rate (0.0 to 1.0)",
                },
                {
                    "name": "quality_score",
                    "dataType": ["number"],
                    "description": "Overall quality score (0.0 to 1.0)",
                },
                {
                    "name": "tags",
                    "dataType": ["string[]"],
                    "description": "Tags: aerospace, medical, automotive, etc.",
                },
                {
                    "name": "created_at",
                    "dataType": ["date"],
                    "description": "Part creation timestamp",
                },
                {
                    "name": "geometry_metadata",
                    "dataType": ["string"],
                    "description": "JSON: volume, surface_area, bounding_box, euler_characteristic",
                },
            ],
        },
        {
            "class": "ManufacturingRule",
            "description": "DFM rule encoded as vector for semantic search",
            "vectorizer": "text2vec-openai",
            "moduleConfig": {
                "text2vec-openai": {
                    "model": "text-embedding-3-small",
                }
            },
            "properties": [
                {
                    "name": "rule_id",
                    "dataType": ["string"],
                    "description": "Unique rule identifier (e.g., cnc_min_hole_diameter)",
                },
                {
                    "name": "process_type",
                    "dataType": ["string"],
                    "description": "Process: cnc | molding | sheet_metal | 3d_print",
                },
                {
                    "name": "rule_description",
                    "dataType": ["text"],
                    "description": "Natural language rule description for semantic search",
                },
                {
                    "name": "parameter",
                    "dataType": ["string"],
                    "description": "Parameter name (e.g., min_hole_diameter, wall_thickness)",
                },
                {
                    "name": "min_value",
                    "dataType": ["number"],
                    "description": "Minimum allowed value",
                },
                {
                    "name": "max_value",
                    "dataType": ["number"],
                    "description": "Maximum allowed value",
                },
                {
                    "name": "unit",
                    "dataType": ["string"],
                    "description": "Unit (mm, degrees, etc.)",
                },
                {
                    "name": "severity",
                    "dataType": ["string"],
                    "description": "Violation severity: error | warning | info",
                },
                {
                    "name": "remediation",
                    "dataType": ["text"],
                    "description": "Guidance for fixing violation",
                },
                {
                    "name": "kb_reference",
                    "dataType": ["string"],
                    "description": "Knowledge base article reference",
                },
            ],
        },
        {
            "class": "AuditLog",
            "description": "Governance and compliance audit trail",
            "vectorizer": "none",
            "properties": [
                {
                    "name": "log_id",
                    "dataType": ["string"],
                    "description": "Unique log entry identifier",
                },
                {
                    "name": "timestamp",
                    "dataType": ["date"],
                    "description": "Request timestamp",
                },
                {
                    "name": "request_method",
                    "dataType": ["string"],
                    "description": "HTTP method (GET, POST, etc.)",
                },
                {
                    "name": "request_path",
                    "dataType": ["string"],
                    "description": "API endpoint path",
                },
                {
                    "name": "status_code",
                    "dataType": ["int"],
                    "description": "HTTP response status",
                },
                {
                    "name": "client_ip",
                    "dataType": ["string"],
                    "description": "Client IP address",
                },
                {
                    "name": "regulated",
                    "dataType": ["boolean"],
                    "description": "Whether request involves regulated data",
                },
                {
                    "name": "regulated_category",
                    "dataType": ["string"],
                    "description": "Regulated category: ITAR | FDA | Aerospace | Medical | etc.",
                },
                {
                    "name": "elapsed_ms",
                    "dataType": ["number"],
                    "description": "Request processing time in milliseconds",
                },
                {
                    "name": "error_message",
                    "dataType": ["string"],
                    "description": "Error message if request failed",
                },
            ],
        },
    ],
}


def get_schema():
    """Return Weaviate schema."""
    return WEAVIATE_SCHEMA
