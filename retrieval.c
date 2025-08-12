#include <math.h>
#include <stdlib.h>

// Computes cosine similarity between two vectors
double cosine_similarity(double *a, double *b, int length)
{
    double dot = 0.0, normA = 0.0, normB = 0.0;
    for (int i = 0; i < length; i++)
    {
        dot += a[i] * b[i];
        normA += a[i] * a[i];
        normB += b[i] * b[i];
    }
    return dot / (sqrt(normA) * sqrt(normB));
}

// Finds index of best match in dataset
int best_match(double *query, double *dataset, int num_vectors, int length)
{
    double max_sim = -1.0;
    int best_idx = -1;
    for (int i = 0; i < num_vectors; i++)
    {
        double sim = cosine_similarity(query, &dataset[i * length], length);
        if (sim > max_sim)
        {
            max_sim = sim;
            best_idx = i;
        }
    }
    return best_idx;
}


