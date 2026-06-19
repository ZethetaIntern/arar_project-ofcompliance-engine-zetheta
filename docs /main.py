from engine import ComplianceEngine

def run_multi_framework_test(engine: ComplianceEngine, transaction: dict, history: list):
    """
    Executes a multi-jurisdictional compliance test across different 
    regulatory frameworks to demonstrate the engine's flexibility.
    """
    print("--- Starting Multi-Framework Compliance Test ---")
    
    # Iterate through frameworks defined in the ComplianceEngine configuration
    for framework in ["UE_AML", "USA_AML"]:
        print(f"\n[Testing: {framework} Framework]")
        
        # Analyze transaction using the class method
        result = engine.analyze_transaction(transaction, framework=framework)
        
        print(f"Rule ID: {result['rule_id']}")
        print(f"Status: {result['status']}")
        print(f"Message: {result['message']}")
    
    print("\n--- Analysis Completed ---")

if __name__ == "__main__":
    # 1. Initialize the professional engine instance
    engine = ComplianceEngine()
    
    # 2. Define test data (12,000€ transaction)
    # Above UE threshold (10,000€) but below USA threshold (15,000€)
    my_tx = {"transaction_id": "TXN-2026-001", "amount": 12000}
    my_history = [1, 2, 3, 4, 5, 6]
    
    # 3. Run the validation test
    run_multi_framework_test(engine, my_tx, my_history)
