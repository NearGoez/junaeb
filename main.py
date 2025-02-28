inoremap ( ()<Esc>i
inoremap { {}<Esc>i
inoremap [ []<Esc>i
inoremap " ""<Esc>i
inoremap ' ''<Esc>i

syntax on
syntax enable
set relativenumber
set number
set guifont=Source\ Code\ Pro\ Regular\ 11
set tabstop=4
set shiftwidth=4
set expandtab
set autoindent
set smartindent
set ruler

call plug#begin()

Plug 'lervag/vimtex'

call plug#end()

let g:vimtex_view_method = 'zathura'
let g:vimtex_view_automatic = 1
let g:vimtex_compiler_method = 'latexmk'
let g:vimtex_compiler_latexmk = {
  \ 'build_dir' : '/home/denis/texbuild',
  \ 'options' : [
  \   '-synctex=1',
  \   '-interaction=nonstopmode',
  \   '-outdir=/home/denis/texbuild',
  \ ],
  \}

autocmd FileType cpp set makeprg=g++\ %\ -o\ \%<.out

function! CompileAndRun()
	if &filetype == 'cpp'
		exec "make"
		if v:shell_error==0
            exec "!xfce4-terminal --command 'bash -c \"./" . expand('%<') . ".out; exec bash\"' &"	
        endif

	elseif &filetype == 'python'
        exec "!xfce4-terminal --command 'bash -c \"python3 " . expand("%") . "; exec bash\"' &"

    endif
endfunction
nnoremap <F5> :call CompileAndRun()<CR>

set clipboard=unnamedplus

highlight Normal ctermbg=none ctermfg=none

            


