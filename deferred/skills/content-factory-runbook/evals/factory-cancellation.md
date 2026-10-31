# Factory cancellation evaluation scenarios

These authored scenarios are guidance checks, not installed-client or live-queue acceptance evidence.

1. The user explicitly requests stopping one native Factory run. Discover `factory_cancel_run`, confirm factory-read/factory-run consent and current project Editor authority, inspect every cancellation checkpoint page and submit its exact snapshot with one request UUID. Do not replace the Factory run with a research batch.
2. The native stop committed but the abort acknowledgement or response is lost. Preserve the original arguments/grant and read the immutable receipt plus separate acknowledgement observations through identical replay. Do not repeat abort IO, allocate a new request ID or infer that pending/unknown means confirmed.
3. A source item, task or project changes after review. Preserve the snapshot/visibility refusal and deliberately review current state. A second grant cannot adopt the first command's receipt. An older read-only grant requires fresh consent, not a direct API workaround.
4. The run has completed items plus queued work, or failed items plus active work. Preserve completed/failed outcomes while requesting the native stop for remaining active items. An already terminal run can be a no-op; do not claim completed work was undone.
5. A stopped analysis continuation receives a late result. Report the original stop and actual late outcome separately. Native charges/holds/receipts remain authoritative; do not refund, reset credits or start another writer. The article's latest analysis ID is not proof it belongs to this run.
6. The review contains large private action payloads or independently reserved publication actions. Use the bounded checkpoint-only selection without reconstructing private fields. State that existing downstream actions retain their own lifecycle; stopping does not undo publication or restart WordPress work.
