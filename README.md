# Tech Challenge Fase 1 — G17

Classificação de câncer de mama (**maligno × benigno**) com Machine Learning, para apoio (não substituição) ao diagnóstico médico.

| Item | Detalhe |
|------|---------|
| **Dataset** | [Breast Cancer Wisconsin (Diagnostic)](https://www.kaggle.com/datasets/uciml/breast-cancer-wisconsin-data/data) |
| **Arquivo local** | `data/raw/data.csv` |
| **Alvo** | `diagnosis` → `M` (maligno) / `B` (benigno) → encoding `1` / `0` |
| **Amostras** | 569 (≈ 357 benignos / 212 malignos) |
| **Notebook** | `notebooks/01_pipeline_eda_preprocessamento.ipynb` |
| **Repo** | https://github.com/LuisEduardoOuroConrado/tech-challenge-fase1-g17 |

---

## Setup rápido

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

Baixe o CSV do Kaggle e salve em `data/raw/data.csv`.

Gerar figuras da EDA (Parte A):

```powershell
.\.venv\Scripts\python.exe src\run_eda.py
```

Abrir o notebook com o kernel `.venv` e rodar as células de cima para baixo.

---

## Divisão do grupo — passo a passo

### Parte A — Luis Conrado (EDA)

1. Documentar o problema e o dataset (contexto clínico).
2. Carregar `data/raw/data.csv` e descrever as colunas.
3. Qualidade dos dados (nulos, duplicatas, `describe`).
4. Balanceamento `B`/`M` + visualizações (distribuições, boxplots, correlação `*_mean`).
5. Exportar gráficos em `reports/figuras/` e insights para o relatório.

**Pronto quando:** notebook (Parte A) revisável + PNGs gerados.

---

### Parte B — Beatriz Honey (pré-processamento)

1. Remover `id` / colunas vazias.
2. Encoding `B=0`, `M=1`.
3. Correlação completa, vs alvo e pares com correlação > 0.9.
4. Split treino/teste **estratificado** (80/20).
5. `Pipeline` com `StandardScaler` (fit só no treino).

**Pronto quando:** `X_train_processed`, `X_test_processed`, `y_train`, `y_test` e pipeline sem leakage.

---

### Parte C — Pedro Henrique Klein (modelagem)

1. Usar os dados processados da Parte B.
2. Treinar **≥ 2** classificadores (ex.: Regressão Logística + Random Forest).
3. Justificar a escolha de cada algoritmo.
4. Manter separação clara treino × teste.

**Pronto quando:** modelos treinados e comparáveis no notebook.

---

### Parte D — Rodrigo Edson Fernandes (avaliação + explicabilidade)

1. Métricas no teste: accuracy, precision, recall, F1, matriz de confusão.
2. Justificar a métrica principal (**recall** da classe maligna).
3. Feature importance e/ou **SHAP**.
4. Discussão crítica: uso prático; médico tem a palavra final.

**Pronto quando:** resultados + interpretação prontos para PDF e vídeo.

---

### Parte E — Alexandre Akio (entregáveis)

1. Consolidar repo, `requirements.txt` e README.
2. Garantir link/instruções do dataset.
3. Montar o **relatório técnico em PDF**.
4. Coordenar/gravar o **vídeo** (≤ 15 min).

**Pronto quando:** GitHub + PDF + link do vídeo.

---

## Entregáveis finais

- Repositório Git com código e este README  
- PDF do relatório técnico (com link do repo)  
- Vídeo ≤ 15 min (YouTube/Vimeo)
