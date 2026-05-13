from sklearn.metrics import roc_auc_score

def get_generalization_gap(source_auc, target_auc):
    """Measures the collapse between Lab (FF++) and Wild (DigiFakeAV) datasets."""
    gap = source_auc - target_auc
    return gap # As seen in the 0.6223 gap result
