from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.step_request_context_type_0 import StepRequestContextType0
    from ..models.tool_call import ToolCall


T = TypeVar("T", bound="StepRequest")


@_attrs_define
class StepRequest:
    """
    Attributes:
        action (None | ToolCall | Unset): Explicit tool call to mediate. When omitted, the sample agent proposes one
            (runs in the background; the step returns 202).
        context (None | StepRequestContextType0 | Unset): Optional contextual facts for this step (see
            AuthorizeActionRequest).
        feed_poison (bool | Unset): When true, an injected malicious signal pushes the sample agent toward an out-of-
            policy action (demo: blocked with proof). Only affects the agent-proposed path. Default: False.
    """

    action: None | ToolCall | Unset = UNSET
    context: None | StepRequestContextType0 | Unset = UNSET
    feed_poison: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.step_request_context_type_0 import StepRequestContextType0
        from ..models.tool_call import ToolCall

        action: dict[str, Any] | None | Unset
        if isinstance(self.action, Unset):
            action = UNSET
        elif isinstance(self.action, ToolCall):
            action = self.action.to_dict()
        else:
            action = self.action

        context: dict[str, Any] | None | Unset
        if isinstance(self.context, Unset):
            context = UNSET
        elif isinstance(self.context, StepRequestContextType0):
            context = self.context.to_dict()
        else:
            context = self.context

        feed_poison = self.feed_poison

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if action is not UNSET:
            field_dict["action"] = action
        if context is not UNSET:
            field_dict["context"] = context
        if feed_poison is not UNSET:
            field_dict["feed_poison"] = feed_poison

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.step_request_context_type_0 import StepRequestContextType0
        from ..models.tool_call import ToolCall

        d = dict(src_dict)

        def _parse_action(data: object) -> None | ToolCall | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                action_type_0 = ToolCall.from_dict(data)

                return action_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ToolCall | Unset, data)

        action = _parse_action(d.pop("action", UNSET))

        def _parse_context(data: object) -> None | StepRequestContextType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                context_type_0 = StepRequestContextType0.from_dict(data)

                return context_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | StepRequestContextType0 | Unset, data)

        context = _parse_context(d.pop("context", UNSET))

        feed_poison = d.pop("feed_poison", UNSET)

        step_request = cls(
            action=action,
            context=context,
            feed_poison=feed_poison,
        )

        step_request.additional_properties = d
        return step_request

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
