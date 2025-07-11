use ruff_diagnostics::Applicability;
use ruff_macros::{ViolationMetadata, derive_message_formats};
use ruff_python_ast as ast;
use ruff_text_size::Ranged;

use crate::checkers::ast::Checker;
use crate::fix::edits::{Parentheses, remove_argument};
use crate::{AlwaysFixableViolation, Fix};

/// ## What it does
/// Checks for classes that inherit from `object`.
///
/// ## Why is this bad?
/// Since Python 3, all classes inherit from `object` by default, so `object` can
/// be omitted from the list of base classes.
///
/// ## Example
///
/// ```python
/// class Foo(object): ...
/// ```
///
/// Use instead:
///
/// ```python
/// class Foo: ...
/// ```
///
/// ## Fix safety
/// This fix is unsafe if it would cause comments to be deleted.
///
/// ## References
/// - [PEP 3115 – Metaclasses in Python 3000](https://peps.python.org/pep-3115/)
#[derive(ViolationMetadata)]
pub(crate) struct UselessObjectInheritance {
    name: String,
}

impl AlwaysFixableViolation for UselessObjectInheritance {
    #[derive_message_formats]
    fn message(&self) -> String {
        let UselessObjectInheritance { name } = self;
        format!("Class `{name}` inherits from `object`")
    }

    fn fix_title(&self) -> String {
        "Remove `object` inheritance".to_string()
    }
}

/// UP004
pub(crate) fn useless_object_inheritance(checker: &Checker, class_def: &ast::StmtClassDef) {
    let Some(arguments) = class_def.arguments.as_deref() else {
        return;
    };

    for base in &*arguments.args {
        if !checker.semantic().match_builtin_expr(base, "object") {
            continue;
        }

        let mut diagnostic = checker.report_diagnostic(
            UselessObjectInheritance {
                name: class_def.name.to_string(),
            },
            base.range(),
        );

        diagnostic.try_set_fix(|| {
            let edit = remove_argument(
                base,
                arguments,
                Parentheses::Remove,
                checker.locator().contents(),
                checker.comment_ranges(),
            )?;

            let range = edit.range();
            let applicability = if checker.comment_ranges().intersects(range) {
                Applicability::Unsafe
            } else {
                Applicability::Safe
            };

            Ok(Fix::applicable_edit(edit, applicability))
        });
    }
}
