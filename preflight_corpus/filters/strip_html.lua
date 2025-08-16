-- Remove any raw HTML blocks/inlines
function RawBlock(el)
  if el.format:match("html") then return {} end
end
function RawInline(el)
  if el.format:match("html") then return {} end
end

-- Drop div/span wrappers but keep their contents
function Div(el) return el.content end
function Span(el) return el.content end