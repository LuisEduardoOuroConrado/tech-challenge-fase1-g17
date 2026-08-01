"""Executa a EDA da Pessoa 1 sem depender do Jupyter no VS Code."""
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

sns.set_theme(style="whitegrid", context="notebook")
plt.rcParams["figure.figsize"] = (10, 5)

ROOT = Path(__file__).resolve().parents[1]
RAW_CSV = ROOT / "data" / "raw" / "data.csv"
FIG_DIR = ROOT / "reports" / "figuras"
FIG_DIR.mkdir(parents=True, exist_ok=True)

df = pd.read_csv(RAW_CSV)
unnamed = [c for c in df.columns if str(c).startswith("Unnamed")]
if unnamed:
    df = df.drop(columns=unnamed)

print(f"Shape: {df.shape}")
print(df["diagnosis"].value_counts().to_string())
print(f"Nulos: {int(df.isna().sum().sum())}")

# 1) Balanceamento
fig, ax = plt.subplots()
sns.countplot(
    data=df,
    x="diagnosis",
    order=["B", "M"],
    hue="diagnosis",
    palette={"B": "#4C9F70", "M": "#C44E52"},
    legend=False,
    ax=ax,
)
ax.set_title("Distribuição das classes (diagnosis)")
ax.set_xlabel("Diagnóstico (B = benigno, M = maligno)")
ax.set_ylabel("Contagem")
fig.tight_layout()
fig.savefig(FIG_DIR / "01_balanceamento_classes.png", dpi=150)
plt.close(fig)

feature_cols = [c for c in df.columns if c not in {"id", "diagnosis"}]
mean_cols = [c for c in feature_cols if c.endswith("_mean")][:6]
ncols, nrows = 3, int(np.ceil(len(mean_cols) / 3))

# 2) Distribuições
fig, axes = plt.subplots(nrows, ncols, figsize=(14, 4 * nrows))
axes = np.array(axes).ravel()
for i, col in enumerate(mean_cols):
    sns.histplot(
        data=df,
        x=col,
        hue="diagnosis",
        kde=True,
        element="step",
        stat="density",
        common_norm=False,
        ax=axes[i],
        palette={"B": "#4C9F70", "M": "#C44E52"},
    )
    axes[i].set_title(col)
for j in range(i + 1, len(axes)):
    axes[j].set_visible(False)
fig.suptitle("Distribuições por diagnóstico", y=1.01)
fig.tight_layout()
fig.savefig(FIG_DIR / "02_distribuicoes_features.png", dpi=150, bbox_inches="tight")
plt.close(fig)

# 3) Boxplots
fig, axes = plt.subplots(nrows, ncols, figsize=(14, 4 * nrows))
axes = np.array(axes).ravel()
for i, col in enumerate(mean_cols):
    sns.boxplot(
        data=df,
        x="diagnosis",
        y=col,
        order=["B", "M"],
        hue="diagnosis",
        palette={"B": "#4C9F70", "M": "#C44E52"},
        legend=False,
        ax=axes[i],
    )
    axes[i].set_title(col)
for j in range(i + 1, len(axes)):
    axes[j].set_visible(False)
fig.suptitle("Boxplots por diagnóstico", y=1.01)
fig.tight_layout()
fig.savefig(FIG_DIR / "03_boxplots_features.png", dpi=150, bbox_inches="tight")
plt.close(fig)

# 4) Correlação
subset = [c for c in feature_cols if c.endswith("_mean")]
corr = df[subset].corr()
fig, ax = plt.subplots(figsize=(12, 10))
sns.heatmap(corr, cmap="vlag", center=0, annot=False, ax=ax)
ax.set_title("Matriz de correlação (features *_mean)")
fig.tight_layout()
fig.savefig(FIG_DIR / "04_correlacao_subset.png", dpi=150)
plt.close(fig)

print("Figuras salvas:")
for p in sorted(FIG_DIR.glob("0*.png")):
    print(" -", p)
