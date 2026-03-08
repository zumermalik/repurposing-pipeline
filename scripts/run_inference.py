import argparse
import logging
from src.data_ingestion.fetch_targets import load_disease_targets
from src.features.build_graph import construct_knowledge_graph
from src.models.gnn_predictor import predict_drug_repurposing
from src.docking.autodock_runner import validate_candidates

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def run_pipeline(disease_id: str, top_k: int = 5):
    logging.info(f"Starting repurposing pipeline for disease ID: {disease_id}")
    
    # Step 1: Ingest Data
    logging.info("Fetching target biological profiles...")
    targets = load_disease_targets(disease_id)
    
    # Step 2: Build Feature Space
    logging.info("Constructing heterogeneous knowledge graph...")
    kg = construct_knowledge_graph(targets)
    
    # Step 3: AI Prediction
    logging.info("Running AI model to predict novel drug-target interactions...")
    candidates = predict_drug_repurposing(kg, top_k=top_k)
    
    # Step 4: Experimental Simulation (Docking)
    logging.info("Running structural docking validation on top candidates...")
    validated_results = validate_candidates(candidates, targets)
    
    logging.info("Pipeline Complete. Top Repurposing Candidates:")
    for result in validated_results:
        print(f"Drug: {result['drug_name']} | Confidence: {result['score']:.4f}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run AI Drug Repurposing Pipeline")
    parser.add_argument("--disease", type=str, required=True, help="Target disease ID (e.g., OMIM or MeSH ID)")
    parser.add_argument("--top_k", type=int, default=5, help="Number of candidates to generate")
    args = parser.parse_args()
    
    run_pipeline(args.disease, args.top_k)
