import pandas as pd

def check_contains(text, keywords):
    return any(k in text.lower() for k in keywords)

def score_tictactoe(row):
    gt = row['ground_truth'].lower()
    pred = row['gemini_response'].lower()

    return {
        'x_correct': int('x is in' in pred and 'x is in' in gt),
        'o_correct': int('o is in' in pred and 'o is in' in gt),
        'position_correct': int(all(pos in pred for pos in gt.split() if pos in ['top', 'middle', 'bottom', 'left', 'right', 'center'])),
        'all_correct': int(pred.strip('.') == gt.strip('.'))
    }

def score_numbers(row):
    gt = row['ground_truth'].lower()
    pred = row['gemini_response'].lower()

    return {
        'number_correct': int(any(str(n) in pred for n in gt.split())),
        'colour_correct': int(check_contains(pred, ['red','blue','yellow','orange','pink','brown'])),
        'size_correct': int(check_contains(pred, ['small','medium','large'])),
        'background_correct': int(check_contains(pred, ['black','white','grey','blue'])),
    }

def score_shapes(row):
    gt = row['ground_truth'].lower()
    pred = row['gemini_response'].lower()

    return {
        'shape_correct': int(check_contains(pred, ['circle','square','triangle','hexagon'])),
        'colour_correct': int(check_contains(pred, ['red','blue','green','yellow','orange','pink','purple'])),
        'position_correct': int(check_contains(pred, ['above','below','left','right','inside','overlapping'])),
        'background_correct': int(check_contains(pred, ['black','white','grey','blue']))
    }

def run_scoring(input_csv, output_csv, domain):
    df = pd.read_csv(input_csv)

    results = []
    for _, row in df.iterrows():
        if domain == 'shapes':
            scores = score_shapes(row)
        elif domain == 'numbers':
            scores = score_numbers(row)
        elif domain == 'tictactoe':
            scores = score_tictactoe(row)

        results.append({**row, **scores})

    pd.DataFrame(results).to_csv(output_csv, index=False)
    print(f"Saved {output_csv}")
