use serde::{Deserialize, Serialize};

use ruff_source_file::{LineColumn, OneIndexed, SourceLocation};

/// Jupyter Notebook indexing table
///
/// When we lint a jupyter notebook, we have to translate the row/column based on
/// [`ruff_text_size::TextSize`] to jupyter notebook cell/row/column.
#[derive(Clone, Debug, Eq, PartialEq, Serialize, Deserialize)]
pub struct NotebookIndex {
    /// Enter a row (1-based), get back the cell (1-based)
    pub(super) row_to_cell: Vec<OneIndexed>,
    /// Enter a row (1-based), get back the row in cell (1-based)
    pub(super) row_to_row_in_cell: Vec<OneIndexed>,
}

impl NotebookIndex {
    pub fn new(row_to_cell: Vec<OneIndexed>, row_to_row_in_cell: Vec<OneIndexed>) -> Self {
        Self {
            row_to_cell,
            row_to_row_in_cell,
        }
    }

    /// Returns the cell number (1-based) for the given row (1-based).
    pub fn cell(&self, row: OneIndexed) -> Option<OneIndexed> {
        self.row_to_cell.get(row.to_zero_indexed()).copied()
    }

    /// Returns the row number (1-based) in the cell (1-based) for the
    /// given row (1-based).
    pub fn cell_row(&self, row: OneIndexed) -> Option<OneIndexed> {
        self.row_to_row_in_cell.get(row.to_zero_indexed()).copied()
    }

    /// Translates the given [`LineColumn`] based on the indexing table.
    ///
    /// This will translate the row/column in the concatenated source code
    /// to the row/column in the Jupyter Notebook.
    pub fn translate_line_column(&self, source_location: &LineColumn) -> LineColumn {
        LineColumn {
            line: self
                .cell_row(source_location.line)
                .unwrap_or(OneIndexed::MIN),
            column: source_location.column,
        }
    }

    /// Translates the given [`SourceLocation`] based on the indexing table.
    ///
    /// This will translate the line/character in the concatenated source code
    /// to the line/character in the Jupyter Notebook.
    pub fn translate_source_location(&self, source_location: &SourceLocation) -> SourceLocation {
        SourceLocation {
            line: self
                .cell_row(source_location.line)
                .unwrap_or(OneIndexed::MIN),
            character_offset: source_location.character_offset,
        }
    }
}
