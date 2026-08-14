# 🎥 Roteiro do vídeo — Tech Challenge Fase 1 (G17)

**Duração alvo:** ≤ 15 min · **Formato:** gravação de tela (notebook + slides) com narração
**Coordenação:** Alexandre Akio

---

## ⏱️ Divisão de tempo (≈ 14 min + folga)

| Bloco | Responsável | Tempo | Conteúdo |
|-------|-------------|:-----:|----------|
| 1. Abertura | Alexandre | 1:00 | Problema, objetivo, dataset, integrantes |
| 2. Parte A — EDA | Luis | 2:30 | Contexto clínico, qualidade dos dados, balanceamento, correlação |
| 3. Parte B — Pré-processamento | Beatriz | 2:30 | Encoding, multicolinearidade, split estratificado, pipeline/scaler |
| 4. Parte C — Modelagem | Pedro | 3:00 | 6 modelos, validação cruzada, escolha do modelo |
| 5. Parte D — Avaliação | Rodrigo | 3:30 | Métricas, matriz de confusão, recall, SHAP |
| 6. Encerramento | Alexandre | 1:30 | Discussão crítica, limitações, conclusão, link do repo |

---

## 🗣️ Pontos de fala por bloco

### 1. Abertura — Alexandre (1:00)
- "Somos o Grupo 17. Nosso desafio: classificar tumores de mama em **maligno** ou **benigno** com Machine Learning, como **apoio** ao diagnóstico."
- Apresentar o dataset **Breast Cancer Wisconsin** (569 amostras, 30 atributos de imagens de FNA).
- Apresentar rapidamente os integrantes e o que cada um fez.
- Reforçar: **o modelo apoia, não substitui o médico.**

### 2. Parte A — EDA — Luis (2:30)
- Contexto clínico: por que diagnóstico precoce importa.
- Qualidade dos dados: **0 nulos, 0 duplicatas** (após remover a coluna vazia `Unnamed: 32`).
- Balanceamento leve: **62,7% benignos / 37,3% malignos** → mostrar Figura 1.
- Distribuições: malignos têm valores maiores de tamanho/irregularidade → Figura 2.
- Correlação alta entre `radius`, `perimeter`, `area` → antecipa multicolinearidade.

### 3. Parte B — Pré-processamento — Beatriz (2:30)
- Remoção do `id` (sem valor preditivo) e encoding do alvo (**B=0, M=1**).
- Multicolinearidade: **21 pares** com correlação > 0,9 (ex.: `radius_mean × perimeter_mean ≈ 0,998`).
- Split **estratificado 80/20** → 455 treino / 114 teste, mantendo a proporção de classes.
- `Pipeline` + `StandardScaler` com **fit só no treino** → evita *data leakage*. (Este é o ponto de ouro para mencionar!)

### 4. Parte C — Modelagem — Pedro (3:00)
- Testamos **6 algoritmos**: Regressão Logística, SVM, Random Forest, KNN, Naive Bayes e Árvore de Decisão.
- Seleção por **validação cruzada estratificada (5-fold)** — **sem usar o teste** para escolher o modelo.
- Mostrar a tabela/gráfico comparativo (Figura 4).
- Escolhido: **Regressão Logística** — melhor recall/F1 da classe maligna + **interpretável**.

### 5. Parte D — Avaliação — Rodrigo (3:30)
- Avaliação final no teste (114 amostras nunca vistas): **acurácia 96,5%**, **recall maligno 92,9%**.
- Matriz de confusão (Figura 5): **1 falso positivo, 3 falsos negativos**.
- **Por que recall é a métrica principal:** falso negativo (maligno dado como benigno) é o erro mais grave clinicamente.
- Explicabilidade: coeficientes + **SHAP** → `concave points`, `radius`, `perimeter`, `area` entre as mais influentes.

### 6. Encerramento — Alexandre (1:30)
- Discussão crítica: resultados promissores, mas **não** prontos para uso clínico direto (dataset limitado, sem validação externa).
- Ferramenta de **apoio/triagem**; decisão final é do médico.
- Mostrar o repositório no GitHub e agradecer.

---

## ✅ Checklist de coordenação (Alexandre)

- [ ] Definir quem grava cada bloco e o **formato** (todos gravam a própria parte OU uma pessoa apresenta o notebook enquanto os outros narram).
- [ ] Padronizar: mesma resolução (1080p), notebook com as saídas já executadas, fonte legível.
- [ ] Cada um cronometra a própria parte **antes** de gravar (evita estourar 15 min).
- [ ] Combinar ferramenta de gravação (OBS, Loom, Zoom gravado ou Meet).
- [ ] Combinar ferramenta de junção/edição (CapCut, Clipchamp, DaVinci) se forem gravações separadas.
- [ ] Fazer uma **passada de ensaio** rápida para checar o tempo total.
- [ ] Subir no **YouTube (não listado)** ou Vimeo e **colar o link no README e no PDF**.
- [ ] Conferir áudio (sem eco/ruído) — costuma ser o que mais derruba nota.

---

## 💡 Dicas rápidas
- Comece cada bloco dizendo **quem é** e **qual parte** está apresentando (ajuda o avaliador).
- Mostre a tela do **notebook rodado** com as saídas visíveis — não só slides.
- Feche sempre reforçando o **recall** e o caráter de **apoio** do modelo (são os pontos que a banca valoriza).
- Deixe ~1 min de folga: 14 min gravados é mais seguro que encostar nos 15.
