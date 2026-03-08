import torch
from src.models.gnn_predictor import RepurposingGNN

def test_gnn_initialization():
    """Ensure the model initializes with correct layer dimensions."""
    model = RepurposingGNN(input_dim=64, hidden_dim=32, output_dim=1)
    assert model is not None
    assert isinstance(model.layer1, torch.nn.Linear)
    assert model.layer1.in_features == 64

def test_gnn_forward_pass_shape():
    """Ensure the model processes mock tensors and returns the expected shape."""
    model = RepurposingGNN(input_dim=10, hidden_dim=5, output_dim=1)
    mock_x = torch.randn(5, 10) # 5 nodes, 10 features each
    mock_edge_index = None # Ignored in our mock linear model
    
    output = model(mock_x, mock_edge_index)
    
    assert output.shape == (5, 1) # Should output a prediction for each node
