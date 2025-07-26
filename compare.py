from embeddings import CountVectorizer, TfidfVectorizer, all_MiniLM_L6_v2
from text_preprocessing import segmentation


class PdfCompare:
    def __init__(self, pdf1: str, pdf2: str):
        self.pdf1 = pdf1
        self.pdf2 = pdf2



    def quick_scan(self, embeddings=2):
        if embeddings == 0:
            return CountVectorizer.count_vectorizer(self.pdf1, self.pdf2)
        elif embeddings == 1:
            return TfidfVectorizer.tfidf_vectorizer(self.pdf1, self.pdf2)
        else:
            return all_MiniLM_L6_v2.all_MiniLM_L6_v2(self.pdf1, self.pdf2)

    
    def moderate_scan(self, embeddings=0, debug=False):
        pdf1_chunks = segmentation(self.pdf1)
        pdf2_chunks = segmentation(self.pdf2)
        from statistics import mean
        
        similarity_scores = []
        # Check if a comparison pair is worth evaluating
        def valid_pair(i, j):
            return len(set(i))>3 and len(set(j))>3 and  i.strip() != "" and j.strip() != "" and len(set(i.split()) | set(j.split())) > 1
        # Define scoring strategy
        def get_similarity(i, j, method):
            try:
                if method == 0:
                    return CountVectorizer.count_vectorizer(i, j)
                elif method == 1:
                    return TfidfVectorizer.tfidf_vectorizer(i, j)
            except ValueError:
                return 0.0
        import re

        def clean(text):
            """
            Cleans input text by:
            - Lowercasing
            - Removing special characters
            - Collapsing multiple whitespaces
            """
            text = text.lower()
            text = re.sub(r'\W+', ' ', text)         # Replace non-word characters with space
            text = re.sub(r'\s+', ' ', text)         # Collapse multiple spaces
            return text.strip()

        if embeddings in (0, 1):
            if len(pdf1_chunks)>len(pdf2_chunks):
                first_chunks=pdf1_chunks
                second_chunks=pdf2_chunks
            else:
                first_chunks=pdf2_chunks
                second_chunks=pdf1_chunks
                
            for i in first_chunks:
                i_clean = clean(i)
                best_score = 0.0
                if len(set(i))<=2:
                    continue
                for j in second_chunks:
                    j_clean = clean(j)
                    if valid_pair(i_clean, j_clean):
                        sim = get_similarity(i_clean, j_clean, embeddings)
                        best_score = max(best_score, sim)
                similarity_scores.append(best_score)

                        
            #k = max(1, int(0.5 * len(similarity_scores)))
            #top_k = sorted(similarity_scores)[-k:]
            #return mean(top_k) if similarity_scores else 0.0
            print(similarity_scores)
            return mean(similarity_scores) if similarity_scores else 0.0
        elif embeddings == 2:
            return all_MiniLM_L6_v2.all_MiniLM_L6_v2(pdf1_chunks, pdf2_chunks)
        # Invalid embedding option
        else:
            raise ValueError("Unsupported embedding value. Use 0, 1, or 2.")


    


    def thorough_scan(self, embeddings=1):
        pdf1_chunks = segmentation(self.pdf1,detailed=True)
        pdf2_chunks = segmentation(self.pdf2,detailed=True)
        from statistics import mean
        
        similarity_scores = []
        # Check if a comparison pair is worth evaluating
        def valid_pair(i, j):
            return len(set(i))>3 and len(set(j))>3 and  i.strip() != "" and j.strip() != "" and len(set(i.split()) | set(j.split())) > 1
        # Define scoring strategy
        def get_similarity(i, j, method):
            try:
                if method == 0:
                    return CountVectorizer.count_vectorizer(i, j)
                elif method == 1:
                    return TfidfVectorizer.tfidf_vectorizer(i, j)
            except ValueError:
                return 0.0
        import re

        def clean(text):
            """
            Cleans input text by:
            - Lowercasing
            - Removing special characters
            - Collapsing multiple whitespaces
            """
            text = text.lower()
            text = re.sub(r'\W+', ' ', text)         # Replace non-word characters with space
            text = re.sub(r'\s+', ' ', text)         # Collapse multiple spaces
            return text.strip()

        if embeddings in (0, 1):
            if len(pdf1_chunks)>len(pdf2_chunks):
                first_chunks=pdf1_chunks
                second_chunks=pdf2_chunks
            else:
                first_chunks=pdf2_chunks
                second_chunks=pdf1_chunks
                
            for i in first_chunks:
                i_clean = clean(i)
                best_score = 0.0
                if len(set(i))<=2:
                    continue
                for j in second_chunks:
                    j_clean = clean(j)
                    if valid_pair(i_clean, j_clean):
                        sim = get_similarity(i_clean, j_clean, embeddings)
                        best_score = max(best_score, sim)
                similarity_scores.append(best_score)

                        
            #k = max(1, int(0.5 * len(similarity_scores)))
            #top_k = sorted(similarity_scores)[-k:]
            #return mean(top_k) if similarity_scores else 0.0
            print(similarity_scores)
            return mean(similarity_scores) if similarity_scores else 0.0
        elif embeddings == 2:
            return all_MiniLM_L6_v2.all_MiniLM_L6_v2(pdf1_chunks, pdf2_chunks)
        # Invalid embedding option
        else:
            raise ValueError("Unsupported embedding value. Use 0, 1, or 2.")

