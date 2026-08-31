# Tech Challenge Fase 1 — G17

Classificação de câncer de mama (**maligno × benigno**) com Machine Learning, para **apoio** (não substituição) ao diagnóstico médico.

> ⚕️ **Aviso:** este é um projeto acadêmico. O modelo é uma ferramenta de **apoio à decisão** — a palavra final é sempre de um profissional de saúde qualificado.

## 🎥 Vídeo de apresentação

**<https://youtu.be/jOU0pZEKgKE>** (≤ 15 min — apresentação completa do pipeline pelo grupo)

## 📊 Resultado principal

Modelo final: **Regressão Logística** (escolhido por validação cruzada, priorizando o *recall* da classe maligna).

| Métrica (classe Maligna) | Teste |
|--------------------------|:-----:|
| Accuracy                 | 0,965 |
| Precision                | 0,975 |
| **Recall** (principal)   | **0,929** |
| F1-score                 | 0,951 |

Matriz de confusão no teste (114 amostras): **TN=71 · FP=1 · FN=3 · TP=39**.

## 🗂️ Dataset

| Item              | Detalhe                                                                                                          |
| ----------------- | -------------------------------------------------------------------------------------------------------------- |
| **Dataset**       | [Breast Cancer Wisconsin (Diagnostic)](https://www.kaggle.com/datasets/uciml/breast-cancer-wisconsin-data/data) |
| **Arquivo local** | `data/raw/data.csv`                                                                                            |
| **Alvo**          | `diagnosis` → `M` (maligno) / `B` (benigno) → encoding `1` / `0`                                                |
| **Amostras**      | 569 (357 benignos / 212 malignos)                                                                              |
| **Atributos**     | 30 numéricos (10 medidas × `_mean` / `_se` / `_worst`)                                                          |
| **Notebook**      | `notebooks/01_pipeline_eda_preprocessamento.ipynb`                                                             |

> 📄 **Por que este dataset?** O raciocínio da escolha, as alternativas avaliadas e as limitações assumidas
> estão no **Anexo A** do [relatório técnico](reports/relatorio_tecnico_g17.pdf) (páginas 8 a 11).

### Como obter o dataset

O CSV **não é versionado** neste repositório (veja `.gitignore`). Para reproduzir:

1. Acesse o [dataset no Kaggle](https://www.kaggle.com/datasets/uciml/breast-cancer-wisconsin-data/data) (é preciso estar logado).
2. Baixe o arquivo `data.csv`.
3. Salve em `data/raw/data.csv` (crie a pasta se ela não existir).

> 💡 Alternativa via CLI: com o [Kaggle CLI](https://github.com/Kaggle/kaggle-api) configurado, rode
> `kaggle datasets download -d uciml/breast-cancer-wisconsin-data -p data/raw --unzip`.

## 🚀 Setup rápido

**Windows (PowerShell):**
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

**Linux / macOS:**
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Baixe o CSV do Kaggle e salve em `data/raw/data.csv` (ver seção acima).

Gerar as figuras da EDA (Parte A) sem abrir o Jupyter:
```bash
python src/run_eda.py
```

Ou abrir o notebook com o kernel `.venv` e rodar as células de cima para baixo.

## 📁 Estrutura do projeto

```
tech-challenge-fase1-g17/
├─ data/
│  └─ raw/            # CSV do Kaggle (não versionado — coloque data.csv aqui)
├─ notebooks/
│  └─ 01_pipeline_eda_preprocessamento.ipynb   # pipeline completo (Partes A–D)
├─ reports/
│  ├─ figuras/                          # figuras geradas pela EDA e avaliação (não versionadas)
│  ├─ relatorio_tecnico_g17.pdf         # ENTREGÁVEL: relatório técnico + Anexo A (11 páginas)
│  └─ roteiro_video.md                  # roteiro usado na gravação
├─ src/
│  └─ run_eda.py                        # gera as figuras da EDA sem depender do Jupyter
├─ requirements.txt
└─ README.md
```

## 🔬 Pipeline (resumo)

1. **EDA** — qualidade dos dados (0 nulos, 0 duplicatas), balanceamento (62,7% B / 37,3% M), distribuições e correlação.
2. **Pré-processamento** — remoção de `id`, encoding do alvo, análise de multicolinearidade (21 pares com correlação > 0,9), split **estratificado** 80/20 (455 treino / 114 teste) e `Pipeline` com `StandardScaler` (fit só no treino → sem *data leakage*).
3. **Modelagem** — comparação de 6 algoritmos (Regressão Logística, SVM, Random Forest, KNN, Naive Bayes, Árvore de Decisão) por **validação cruzada estratificada (5-fold)** no treino.
4. **Avaliação e explicabilidade** — métricas no teste, matriz de confusão, justificativa do *recall* como métrica principal, importância das features (coeficientes) e **SHAP**.

## 👥 Divisão do grupo

| Parte | Responsável | Foco | Status |
|-------|-------------|------|:------:|
| **A** | Luis Conrado | Dataset, contexto e EDA | ✅ |
| **B** | Beatriz Honey | Encoding, correlação, split, scaler e pipeline | ✅ |
| **C** | Pedro Henrique Klein | Modelagem (≥ 2 algoritmos) | ✅ |
| **D** | Rodrigo Edson Fernandes | Avaliação, métricas e explicabilidade (SHAP) | ✅ |
| **E** | Alexandre Akio | Integração, documentação, PDF e vídeo | ✅ |

## 📦 Entregáveis finais

O enunciado pede **um único PDF** de entrega: é o
[`reports/relatorio_tecnico_g17.pdf`](reports/relatorio_tecnico_g17.pdf), que reúne tudo abaixo.

| Entregável | Onde |
|------------|------|
| PDF de entrega (relatório técnico + Anexo A) | [`reports/relatorio_tecnico_g17.pdf`](reports/relatorio_tecnico_g17.pdf) |
| Link do repositório Git | Capa do PDF · <https://github.com/LuisEduardoOuroConrado/tech-challenge-fase1-g17> |
| Código-fonte e README com instruções | Este repositório |
| Dataset (link de download) | [Kaggle — Breast Cancer Wisconsin](https://www.kaggle.com/datasets/uciml/breast-cancer-wisconsin-data/data) |
| Resultados (gráficos e análises) | 5 figuras no PDF · [notebook executado](notebooks/01_pipeline_eda_preprocessamento.ipynb) |
| Relatório técnico (EDA, pré-proc., modelos, interpretação) | Seções 1 a 9 do PDF |
| Justificativa da escolha do dataset | Anexo A do PDF (páginas 8 a 11) |
| Vídeo de apresentação (≤ 15 min) | <https://youtu.be/jOU0pZEKgKE> |
| Dockerfile | Não se aplica — o projeto não usa Docker |
